import random

def sorsol() -> list:
    hány = int(input("Hány számot sorsoljak?"))
    mettől = int(input("Mettől sorsoljak?"))
    meddig = int(input("Meddig sorsoljak?"))
    lista = []
    for x in range(hány):
        lista.append(random.randint(mettől, meddig))
    lista.sort()
    return lista 

számlista = sorsol()
számlista2 = sorsol()
print(f"Lista elemei: {számlista}")