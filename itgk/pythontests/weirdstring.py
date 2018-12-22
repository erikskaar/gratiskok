def to_weird_case(string):
    string = list(string.lower())
    for x in range(len(string)):
        if x%2==0 and string[x].isalpha():
            string[x] = string[x].upper()
        else:
           continue
    return "".join(string)

print(to_weird_case("This is a test"))