def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    f.close()
    return innhold
print(read_from_file('my_file.txt'))
