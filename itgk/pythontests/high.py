def high(text):
    text = list(text.split(' '))
    for x in range(len(text)):
        for j in range(len(text[x])):
            text[x][j] = str(ord((text[x][j])-96))
    return text



print(high("hello world waddup"))