def write_to_file(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close

def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    return innhold
    f.close()

def main():
    readOrWrite = input("Do you want to read or write?\n")
    if readOrWrite == "write":
        whatToWrite = input("What do you want to write?\n")
        write_to_file(whatToWrite)
        print(whatToWrite + "was written to file.")
        main()
    elif readOrWrite == "read":
        print(read_from_file('my_file.txt'))
        main()
    elif readOrWrite == "done":
        print("You are done.")
        return

main()