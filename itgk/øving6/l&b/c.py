def median(list):
    list.sort()
    return list[int(len(list)/2)]

newList = [1,2,4,5,7,9,10]
newList2 = [1,4,2,5,3]
print(median(newList2))