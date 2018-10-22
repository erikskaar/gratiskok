number_list = []
even_list = []
odd_list = []
for x in range(100):
    if(x%2==0):
        even_list.append(x)
    else:
        odd_list.append(x)

for x , item in enumerate(odd_list):
    number_list.append(odd_list[x])
    number_list.append(even_list[x])

print(number_list)