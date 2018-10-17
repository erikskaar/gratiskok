def komparativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
  
### TILLEGG 1, ny funksjon, kommer her:
 
def superlativ(adj):
    if len(adj) >= 8: # unøyaktig
        svar = "mest " + adj
    else:
        svar = adj + "est"
    return svar

def main():
    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")
    print("Jeg er faktisk " + superlativ(adj) + " i hele verden.")

    adj = input("Skriv inn et adjektiv: ")
    svar = input("Hva er komparativ for " + adj + "? ")
    fasit = komparativ(adj)
    if svar == fasit:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit)

    svar = input("Hva er superlativ for " + adj + "? ")
    fasit = superlativ(adj)
    if svar == fasit:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit)
main()