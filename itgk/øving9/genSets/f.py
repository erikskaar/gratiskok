def allUnique(lst):
    testSet = set(lst)
    if len(testSet) == len(lst):
        return True
    else:
        return False

print(allUnique([1,3,2,6,8]))
print(allUnique([1,3,5,2,3,7]))