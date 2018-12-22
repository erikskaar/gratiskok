def find_even_index(arr):
    newSum = sum(arr)
    midSplit = newSum/2
    counter = 0
    for x in range(len(arr)):
        counter += arr[x]
        if counter >= midSplit:
            return x

print(find_even_index([3,2,1,1,3,2]))