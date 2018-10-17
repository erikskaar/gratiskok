def times(n):
    return (1+1/pow(n,2))

def myFunc(tol):
    prod = 2
    oldProd = 0
    n = 1
    while prod - oldProd > tol:
        n += 1
        oldProd = prod
        prod = prod*times(n)
    return prod, n
tol = float(input("Toleranse:"))
print(myFunc(tol))