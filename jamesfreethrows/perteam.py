import requests
import itertools

playerID = 2544
season = "2015-16"
seasonType = "Regular Season"
headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}



'''
    _get = requests.get('http://stats.nba.com/stats/commonplayerinfo', params={'PlayerID': 2544}, headers=headers)
    _get.raise_for_status()
    global name, lastname
    name = (_get.json()['resultSets'][0]['rowSet'])[0][2]
    lastname = (_get.json()['resultSets'][0]['rowSet'])[0][3] 24
'''
def grpSort(matrix, key):

    return itertools.groupby(sorted(matrix, key= lambda s: s[key]), key= lambda s: s[key])

def getGames(playerID, season, seasonType):

    _get = requests.get('http://stats.nba.com/stats/playergamelog', params={'PlayerID': playerID, 'Season':season, 'SeasonType':seasonType}, headers=headers)
    _get.raise_for_status()
    games = _get.json()['resultSets'][0]['rowSet']
    temp = [[row[4].encode("utf-8")[4:].replace("vs. ", "").replace("@ ", ""), row[24]] for row in games]

    return temp

allgames = []
for i in range(3, 16):
    allgames.extend(getGames(playerID, "20%02d-%02d" % (i, i + 1), seasonType))

temp = []
for a in grpSort(allgames, 0):
    sum = 0
    length = 0
    name = ""
    for b in a[1]:
        sum += b[1]
        length += 1
        name = b[0]
    temp.append([name, float(sum)/length, length])

for a in temp:
    print "%s | %02.02f | %d" % (a[0], a[1], a[2])
