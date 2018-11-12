my_set = set()

for i in range(20):
    if i%2!=0:
        my_set.add(i)


my_set2 = set()

for i in range(10):
    if i%2!=0:
        my_set2.add(i)


my_set3 = set()

my_set3 = my_set-my_set2
print(my_set, my_set2, my_set3)