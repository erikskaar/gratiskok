def alphabet_position(text):
    text = text.lower()
    text = list(text)
    text = list(filter(str.isalpha, text))
    newText = []
    for x in range(len(text)):
        if text[x].isalpha():
            text[x] = str(ord(text[x])-96)


    newText = list(filter(str.strip, text))
    newText = list(filter(str.isdigit, text))
    return " ".join(newText)

print(alphabet_position("25 30 23"))