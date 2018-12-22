def disemvowel(string):
    vowels = ['a','e', 'i', 'o', 'u']
    for x in range(len(vowels)):
        string = string.split(vowels[x])
        string = "".join(string)
    return string

print(disemvowel("This website is for losers LOL"))