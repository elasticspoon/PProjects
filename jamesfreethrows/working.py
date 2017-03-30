import pickle


postseason = pickle.load(open( "post.p.p", "rb" ))
regularseason = pickle.load(open( "reg.p", "rb" ))
list = []
list.extend(postseason)
list.extend(regularseason)


def add(one, two):

    return [one[a] + two[a] for a in range(14)]

def calculate(matrix):

    totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for game in matrix:

        totals = add(totals, game["stats"])
    temp = []
    for i in range(7):
        if totals[2 * i] == 0 and totals[2 * i + 1] == 0:
            temp.append(0)
        else:
            temp.append((float(totals[2 * i])/(totals[2 * i] + totals[2 * i+1])) * 100)
        temp.append(totals[2 * i] + totals[2 * i + 1])

    return temp

def getResults(season, seasonType, location, opp, matrix):

    final = []

    for game in matrix:
        if "any" in season or game["season"] == season:
            pass
        else:
            continue
        if "any" in seasonType or game["seasonType"] == seasonType:
            pass
        else:
            continue
        if "any" in location or game["location"] == location:
            pass
        else:
            continue
        if "any" in opp or game["opp"] == opp:
            pass
        else:
            continue
        final.append(game)

    res = calculate(final)

    print "%s %s %s vs %s \nFirst Ft. %02.02f Percent on %d Attempts \nSecond Ft. %02.02f " \
          "Percent on %d Attempts \nThird Ft. %02.02f Percent on %d Attempts" \
          "\nTechnical Ft. %02.02f Percent on %d Attempts\nFirst Flagrant Ft. %02.02f Percent on %d Attempts" \
          "\nSecond Ft. %02.02f Percent on %d Attempts\nClear Path Ft. %02.02f Percent on %d Attempts\n" \
          % (season, seasonType, location, opp, res[0], res[1], res[2], res[3], res[4], res[5], res[6],
             res[7], res[8], res[9], res[10], res[11], res[12], res[13])

#getResults(season, seasonType, location, opp, matrix):
'''
for a in range(3, 16):
    print("Season 20%02d-%02d" % (a, a + 1))
    getResults("20%02d-%02d" % (a, a + 1), "any", "any", "any", list)
'''
getResults("any", "any", "any", "any", list)
