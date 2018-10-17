# skriv funksjonen cmyk2rgb() her øverst
def cmyk2rgb(C, M, Y, K):
    i = round((255 * (1-C) * (1-K)), 0)
    j = round((255 * (1-M) * (1-K)), 0)
    k = round((255 * (1-Y) * (1-K)), 0)
    return (i, j, k)

  
print("Oppgi farge i CMYK og få det konvertert til RGB.")
C = float(input("C: "))
M = float(input("M: "))
Y = float(input("Y: "))
K = float(input("K: "))
R, G, B = cmyk2rgb(C, M, Y, K)
print("Som RGB:", R, G, B)

# viser fargen på skjermen:
from turtle import colormode, bgcolor
colormode(255)
bgcolor(int(R), int(G), int(B))
input()