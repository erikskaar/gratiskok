def sliceTime(list):
    result = ""
    for i in range(len(list)):
        current = list[i]
        result += current[-2::]
    return result

myList = ["sabel","kan","mestr","kuleis"]
print(sliceTime(myList))