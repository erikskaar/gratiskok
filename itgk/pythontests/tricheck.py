def narcissistic(num1):
    num2 = list(str(num1))
    array = []
    for x in range(len(num2)):
        array.append(int(num2[x])**len(num2))
    if sum(array) == num1:
        return 1
    else:
        return 0
print(narcissistic(23))