def get_sum(a,b):
        list = []
        if a!=b:
                if a>b:
                        for x in range(a,b):
                                list.append(x)
                        list.append(b)
                elif a<b:
                        for x in range(a,b,-1):
                                list.append(x)
                        list.append(a)
                return sum(list)
        elif a==b:
                return a
        


print(get_sum(0,-1))
print(sum(range(0,-1)))