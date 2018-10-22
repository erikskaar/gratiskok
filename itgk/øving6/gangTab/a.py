myList = [1,2,3,4,5,6,7,8,9]
belThresh = []
aboThresh = []
def separate(numbers, threshold):
    for x, item in enumerate(numbers):
        if(numbers[x]>=threshold):
            aboThresh.append(numbers[x])
        else:
            belThresh.append(numbers[x])
    return belThresh, aboThresh
print(separate(myList, 5))