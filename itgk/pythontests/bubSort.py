
unsortedList = [5,3,23,4,1,6,8,2,7,9,23,58,23,13,43,56,34,42,54,34,3,2,5,7,1,8,9,5,3,23,4,1,6,8,2,7,9,23,58,23,13,43,56,34,42,54,34,3,2,5,7,1,8,9,5,3,23,4,1,6,8,2,7,9]



def bubSort(list):
    for x in range(len(list)-1):
        if list[x] > list[x+1]:
            list[x], list[x+1] = list[x+1], list[x]
            bubSort(list)
        else:
            continue
    return list

print(bubSort(unsortedList))