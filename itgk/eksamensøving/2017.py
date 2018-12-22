def formatTime(seconds):
    hours = seconds//3600
    mins = seconds % 3600 //60
    s = seconds %60
    if hours<10:
        hours = '0'+str(hours)
    if mins<10:
        mins = '0'+str(mins)
    if s<10:
        s = '0'+str(s)
    result = str(hours) + ':' + str(mins) + ':' + str(s)
    return result

#print(formatTime(12305))

def valuesDecember():
    first = 3*60*60 + 18*60
    period = 12*60*60 + 25*60 + 12
    return first, period

#print(valuesDecember())

def genTides():
    highs = []
    lows = []
    first, period = valuesDecember()
    secsInMonth = 60*60*24*31
    tide = first
    while tide<secsInMonth:
        lows.append(tide)
        highs.append(tide+period//2)
        tide += period
    
    return highs, lows

#print(genTides())

highs, lows = genTides()
def genTidesStr(tideList):
    returnList = []
    day = 60*60*24
    for x in range(len(tideList)):
        whichDay = int(tideList[x]/day) +1
        remainSecs = tideList[x]-(day*(whichDay-1))
        formattedSecs = formatTime(remainSecs)
        returnList.append(str(whichDay)+ " " + formattedSecs)

    return returnList

#print(genTidesStr(lows))

def checkTides(dayInMonth):
    highs, lows = genTides()
    secsInDay = 60*60*24
    startTime = dayInMonth*secsInDay + 9*3600
    endTime = startTime + 4*3600
    
    for item in highs:
        if startTime <= item <= endTime:
            print('high tide at ' + formatTime(item % secsInDay))
            return
    for item in lows:
        if startTime <= item <= endTime:
            print('low tide at ' + formatTime(item % secsInDay))
            return
    print('no tides')
    
print(checkTides(12))

def file_to_table(filename):
    table = []
    f = open(filename, "r")
    a = f.read().strip('\n')
    return a


#print(file_to_table("table.txt"))