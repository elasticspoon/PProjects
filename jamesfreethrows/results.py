import pickle

postseason = pickle.load(open( "post.p", "rb" ))
regularseason = pickle.load(open( "reg.p", "rb" ))


results = []


def add(one, two):

    return [one[a] + two[a] for a in range(6)]

def calc(matrix):

    temp = []
    for i in range(3):
        if matrix[2 * i] == 0 and matrix[2 * i+1] == 0:
            temp.append(0)
        else:
            temp.append((float(matrix[2 * i])/(matrix[2 * i] + matrix[2 * i+1])) * 100)
    #return "First: %f %  Second: %f %  Third %f %" % (temp[0], temp[1], temp[2])
    return temp

total = []
total.extend(postseason)
total.extend(regularseason)

for season in total:
    for game in season[1]:
        loc = "away" if "@" in game[1] else "home"
        opp = game[1].replace("CLE vs. ", "").replace("CLE @ ", "").replace("MIA vs. ", "").replace("MIA @ ", "")
        seasonType = "playoffs" if "Playoffs" in season[0] else "regular"
        seas = season[0].replace("Season ", "").replace(" Playoffs", "").replace(" Regular Season", "")
        results.append({"season" : seas, "seasonType" : seasonType, "location" : loc, "make1" : game[0][0], "opp" : opp,
                        "miss1" : game[0][1], "make2" : game[0][2], "miss2" : game[0][3], "make3" : game[0][4], "miss3" : game[0][5]})

pickle.dump(results, open("final.p", "wb"))


"""
for season in postseason:
    home = []
    away = []
    hometotals = [0, 0, 0, 0, 0, 0]
    awaytotals = [0, 0, 0, 0, 0, 0]
    print season
    if len(season[1]) == 0:
        continue
    for game in season[1]:
        if "@" in game[1]:
            game[1] = game[1].replace("CLE @ ", "")
            game[1] = game[1].replace("MIA @ ", "")
            home.append(game)
            hometotals = add(hometotals, game[0])
        else:
            game[1] = game[1].replace("CLE vs. ", "")
            game[1] = game[1].replace("MIA vs. ", "")
            away.append(game)
            awaytotals = add(hometotals, game[0])
    #print "First: %02.2f  Second: %02.2f  Third %02.2f" % (calc(hometotals)[0], calc(hometotals)[1], calc(hometotals)[2])
    #print "First: %02.2f  Second: %02.2f  Third %02.2f" % (calc(awaytotals)[0], calc(awaytotals)[1], calc(awaytotals)[2])
"""