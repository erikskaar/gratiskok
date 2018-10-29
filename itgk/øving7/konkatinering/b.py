def concate(list):
    result = ""
    for i in range(len(list)):
        result += list[i]
    return result

myList = ["abc","defg","hijklm","nop"]
print(concate(myList))