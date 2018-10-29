def repeat(character):
    for i in range(8):
        print(character*i)
    for i in range(8,0,-1):
        print(character*i)
repeat('Z')