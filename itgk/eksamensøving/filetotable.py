#def file_to_table(filename):
# table = []
# f = open(filename,'r')
# for line in f:
#    line = line.strip() # Remove white spaces
#    data = line.split(',')
# for i in range(6): # Pick out date (3 digits) and time (3 digits)
#    data[i]=int(data[i])
#    table.append(data)
# f.close()
# return table
#print(file_to_table("table.txt"))


def file_to_table(filename):
    table = []
    f = open(filename, "r")
    a = f.read().strip('\n')
    return a
print(file_to_table("table.txt"))