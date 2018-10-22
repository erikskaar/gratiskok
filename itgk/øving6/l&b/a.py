def is_six_at_edge(list):
    return (list[0]==6 or list[-1]==6):


newList = [1,2,3,4,5,6]
newList2 = [1,2,3,4,5,6, 7]
print(is_six_at_edge(newList))
print(is_six_at_edge(newList2))