def in_array(array1, array2):
    resultArray = []
    for x in range(len(array1)):
        for j in range(len(array2)):
            if array2[j] in array1[x]:
                resultArray.append(array2[j])
    return list(set(resultArray))


print(in_array(["lively", "alive", "harp", "sharp", "armstrong"],["arp", "live", "strong"]))