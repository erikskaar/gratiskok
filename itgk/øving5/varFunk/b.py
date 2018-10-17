# skriv funksjonen din her
def knop2km_t(x):
    x = x*0.514444444444
    x = x*3.6 
    return x
  
# skript
knop = float(input("Oppgi fart i knop:"))
km_t = knop2km_t(knop)
print("Det blir", round(km_t, 2), "km/t")