number_list = []
even_list = []
odd_list = []
reversed_list = []
for x in range(100):
    if(x%2==0):
        even_list.append(x)
    else:
        odd_list.append(x)

for x , item in enumerate(odd_list):
    number_list.append(odd_list[x])
    number_list.append(even_list[x])

length = len(number_list)+1

for x in range(length):
    reversed_list.append(number_list[-x])

del reversed_list[0]
print(reversed_list)
print(len(reversed_list))