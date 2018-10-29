def concate(list):
    result = []
    for i in range(len(list)):
        result.append(list[i][0])
    return result

myList = ["UKA","lever","videre"]
print(concate(myList))