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


def getFreeThrows(gameId):

    _get = requests.get('http://stats.nba.com/stats/playbyplay', params={"GameID":gameId,"StartPeriod":1,"EndPeriod":10}, headers=headers)
    _get.raise_for_status()
    pbp = _get.json()['resultSets'][0]['rowSet']
    filtered = []
    for a in pbp:
        if a[9] != None:
            if "Dunk" in a[9].encode("utf-8"):
                filtered.append(a[9])
        if a[7] != None:
            if "Dunk" in a[7].encode("utf-8"):
                filtered.append(a[7])

    return len(filtered) == 0 and len(pbp) != 0


def finalThing(season):

    seasonal = []
    for a in range(0, 2000):

        if getFreeThrows("002%02d0%04d" % (season, a)):
            seasonal.append("002%02d0%04d" % (season, a))

        #final.append(["Season 20%02d-%02d %s" % (a, a+1, seasonType), seasonal])
    return seasonal

print finalThing(15)
#print getFreeThrows("0021600458")






