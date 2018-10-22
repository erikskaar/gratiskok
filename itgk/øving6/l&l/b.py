number_list = []
div_list = []
for x in range (100):
    number_list.append(x)
    if (x%3==0 or x%10==0):
        div_list.append(x)
print(number_list)
print(sum(div_list))
