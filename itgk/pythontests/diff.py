def array_diff(a, b):
    for j in range(len(b)):
        if b[j] in a:
            a = [x for x in a if x != b[j]]
    return a

print(array_diff([1,2,2,2,3],[2]))