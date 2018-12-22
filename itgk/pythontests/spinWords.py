def spinWords(string):
    string = list(string.split(" "))
    for x in range(len(string)):
        if len(string[x])>5:
            string[x] = string[x][::-1]
    return " ".join(string)

print(spinWords("ayylmao hei du"))
