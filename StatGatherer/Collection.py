import requests
import pickle
import argparse

headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}


def getDashBoardInfo(playerId, measureType, perMode):

    _get = requests.get('http://stats.nba.com/stats/playerdashboardbyyearoveryear',
                        params={
                            "DateFrom" : "",
                            "DateTo" : "",
                            "GameSegment" : "",
                            "LastNGames" : 0,
                            "LeagueID" : "00",
                            "Location" : "",
                            "MeasureType" : measureType,
                            "Month" : 0,
                            "OpponentTeamID" : 0,
                            "Outcome" : "",
                            "PORound" : 0,
                            "PaceAdjust" : "N",
                            "PerMode" : perMode,
                            "Period" : 0,
                            "PlayerID" : playerId,
                            "PlusMinus" : "N",
                            "Rank" : "N",
                            "Season" : "2016-17",
                            "SeasonSegment" : "",
                            "SeasonType" : "Regular Season",
                            "ShotClockRange" : None,
                            "VsConference" : "",
                            "VsDivision" : ""},
                        headers=headers)
    _get.raise_for_status()
    '''pbp = _get.json()['resultSets'][1]['rowSet']'''
    pbp = _get.json()['resultdocumentSets'][1]['headers']

    return pbp

print getDashBoardInfo(1626157, "Base", "PerGame")