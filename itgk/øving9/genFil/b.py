def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    return innhold
    f.close()
print(read_from_file('my_file.txt'))
