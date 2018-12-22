parties = ['TeaParty', 'CoffeeParty', 'MilkParty', 'HouseParty', 'BeachParty']
def initElection(parties):
    votes = []
    for x in range(92):
        votes.append([0]*len(parties))
    return votes
#print(initElection(parties))

def updateElection(election, district, results):
    for x in range(len(results)):
        election[district][x] += results[x]
    return election

#print(updateElection(initElection(parties), 3, [1232,2323,4343,2323,0]))

def printLeadP(election, parties):
    results = [0,0,0,0,0]
    for x in range(len(election)):
        for j in range(len(parties)):
            results[j] += election[x][j]

    votes = max(results)
    winner = parties[results.index(votes)]
    toPrint = winner + " is leading the election with " + str(votes) + " votes"
    return toPrint

print(printLeadP(updateElection(initElection(parties), 3, [1232,2323,4343,2323,0]), parties))