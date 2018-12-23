sortedList = []

for x in range(50, 360, 4):
    sortedList.append(x)

def binSearch(sort_list, num):
    if len(sort_list)>2:
        pivot = int(len(sort_list)/2)
        if sort_list[pivot]>num:
            del sort_list[pivot:-1]
            binSearch(sort_list,num)
        pivot = int(len(sort_list)/2)
        if sort_list[pivot]>num:
            del sort_list[pivot:-1]
            binSearch(sort_list,num)
        elif sort_list[pivot]<num:
            del sort_list[0:pivot]
            binSearch(sort_list,num)
        elif sort_list[pivot] == num:
            return True
        binSearch(sort_list, num)
    if len(sort_list) == 2 or len(sort_list) == 1:
        for x in sort_list:
            if x == num:
                return True
        return False

print(binSearch(sortedList, 222))
print(sortedList)
#print(sortedList)
#binsøk(liste,num):
