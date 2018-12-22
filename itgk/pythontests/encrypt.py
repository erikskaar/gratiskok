def encrypt_this(text):
    text = list(text.split(' '))
    for x in range(len(text)):
        text[x][0] = str(ord(text[x][0])-96)
    return text


print(encrypt_this("Hello world"))