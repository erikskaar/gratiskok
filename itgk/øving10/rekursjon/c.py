def find_smallest_element(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        for x in range(len(numbers)):
            if numbers[x]<numbers[x+1]:
                return numbers[x] 


print(find_smallest_element([5,3,2,6]))