# skriv funksjonen din her
def imp2cm(x, y):
    x = x*12*2.54
    y = y*2.54
    
    return x + y
 
 
# skript
fot = int(input("Oppgi antall fot: "))
tommer = int(input("Oppgi antall tommer: "))
cm = imp2cm(fot, tommer)
print("Det blir ", cm, "cm")