# Skriv funksjonen din her
  
def absol(x):
    if x>=0:
        result = x
    elif x<0:
        result = -x
    return result
  
# skript for å teste funksjonen:
print("Absoluttverdien til 5 er", absol(5))
print("Absoluttverdien til -3 er", absol(-3))
print("Absoluttverdien til 0 er", absol(0))