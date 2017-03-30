import requests
import pickle
import argparse

headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}
name = ""
fullname = ""

def getFreeThrows(gameId):

    _get = requests.get('http://stats.nba.com/stats/playbyplay',
                        params={
                            "GameID":gameId,
                            "StartPeriod":1,
                            "EndPeriod":10},
                        headers=headers)
    _get.raise_for_status()
    pbp = _get.json()['resultSets'][0]['rowSet']

    return pbp


def finalThing(season):

    seasonal = []
    for a in range(0, 1250):
        print "game %d" % a
        seasonal.append(getFreeThrows("002%02d0%04d" % (season, a)))

    return seasonal
last = []
for a in range(15):
    pickle.dump(finalThing(a), open("season%d_reg.p" % a, "wb"))

pickle.dump(last, open("allgamelogs_reg.p", "wb"))






