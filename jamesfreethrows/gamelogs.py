import requests
import pickle
import argparse

headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}
name = ""
fullname = ""

def getColumn(matrix, i):
    temp = []
    for row in matrix:
        if isinstance(row[i], basestring):
            temp.append(row[i].encode("utf-8"))
        else:
            temp.append(row[i])
    return temp

def getGames(playerID, season, seasonType):

    _get = requests.get('http://stats.nba.com/stats/commonplayerinfo', params={'PlayerID': 2544}, headers=headers)
    _get.raise_for_status()
    global name, lastname
    name = (_get.json()['resultSets'][0]['rowSet'])[0][2]
    lastname = (_get.json()['resultSets'][0]['rowSet'])[0][3]

    _get = requests.get('http://stats.nba.com/stats/playergamelog', params={'PlayerID': playerID, 'Season':season, 'SeasonType':seasonType}, headers=headers)
    _get.raise_for_status()
    games = _get.json()['resultSets'][0]['rowSet']
    temp = []
    for row in games:
        temp2 = []
        if isinstance(row[2], basestring):
            temp2.append(row[2].encode("utf-8"))
        else:
            temp2.append(row[2])
        if isinstance(row[4], basestring):
            temp2.append(row[4].encode("utf-8"))
        else:
            temp2.append(row[4])
        temp.append(temp2)
    return temp


def getFreeThrows(gameId, Opp, playerId):

    _get = requests.get('http://stats.nba.com/stats/playbyplay', params={"GameID":gameId,"StartPeriod":1,"EndPeriod":10}, headers=headers)
    _get.raise_for_status()
    pbp = _get.json()['resultSets'][0]['rowSet']
    filtered = []
    for a in pbp:
        if "@" in Opp:
            if a[9] == None:
                continue
            if "%s Free Throw" % name in a[9].encode("utf-8"):
                filtered.append(a[9])
        else:
            if a[7] == None:
                continue
            if "%s Free Throw" % name in a[7].encode("utf-8"):
                filtered.append(a[7])


    return [grossEval(filtered), Opp]

def grossEval(matrix):

    make1 = 0
    make2 = 0
    make3 = 0
    miss1 = 0
    miss2 = 0
    miss3 = 0
    misst = 0
    maket = 0
    makeflg1 = 0
    makeflg2 = 0
    missflg1 = 0
    missflg2 = 0
    makecp = 0
    misscp = 0


    for play in matrix:
        if "MISS" in play:
            if "Free Throw 1 of 3" in play or "Free Throw 1 of 2" in play or "Free Throw 1 of 1" in play:
                miss1 += 1
                continue
            if "Free Throw 2 of 3" in play or "Free Throw 2 of 2" in play:
                miss2 += 1
                continue
            if "Free Throw 3 of 3" in play:
                miss3 += 1
                continue
            if "Technical" in play:
                misst += 1
                continue
            if "Flagrant 1 of 1" in play or "Flagrant 1 of 2" in play:
                missflg1 += 1
                continue
            if "Flagrant 2 of 2" in play:
                missflg2 += 1
                continue
            if "Clear Path" in play:
                misscp += 1
                continue
        else:
            if "Free Throw 1 of 3" in play or "Free Throw 1 of 2" in play or "Free Throw 1 of 1" in play:
                make1 += 1
                continue
            if "Free Throw 2 of 3" in play or "Free Throw 2 of 2" in play:
                make2 += 1
                continue
            if "Free Throw 3 of 3" in play:
                make3 += 1
                continue
            if "Technical" in play:
                maket += 1
                continue
            if "Flagrant 1 of 1" in play or "Flagrant 1 of 2" in play:
                makeflg1 += 1
                continue
            if "Flagrant 2 of 2" in play:
                makeflg2 += 1
                continue
            if "Clear Path" in play:
                makecp += 1
                continue

    return [make1, miss1, make2, miss2, make3, miss3, maket, misst, makeflg1, missflg1, makeflg2, missflg2, makecp, misscp]

def finalThing(playerId, seasonS, seasonE, seasonType):

    final = []
    #totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in range(seasonS, seasonE + 1):
        temp = getGames(2544, '20%02d-%02d' % (a, a+1), seasonType)
        seasonal = []
        for b in temp:
            ft = getFreeThrows(b[0], b[1], playerId)
            seasonal.append(ft)
            #totals = add(totals, ft[0])
            loc = "away" if "@" in ft[1] else "home"
            opp = ft[1][4:].replace("vs. ", "").replace("@ ", "")
            final.append({"season" : '20%02d-%02d' % (a, a+1), "seasonType" : seasonType, "location" : loc, "opp" : opp,
                        "stats" : ft[0]})

        #final.append(["Season 20%02d-%02d %s" % (a, a+1, seasonType), seasonal])
    return final

def run(a):

    playerId, seasonStart, seasonEnd, seasonType, outfile = a
    pickle.dump(finalThing(int(playerId), int(seasonStart), int(seasonEnd), seasonType), open("%s.p" % outfile, "wb"))


parser = argparse.ArgumentParser()
parser.add_argument('-r', '--run', nargs = 5,
                    help='Args: playerId, seasonStart, seasonEnd, seasonType, outfile')

args = parser.parse_args()
run(args.run)


