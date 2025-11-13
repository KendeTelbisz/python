import random

def sorsol(hány = int(5), mettől = int(1), meddig = int(90)) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
        lista.sort()
    return lista
    
for x in range(52):
    számlista = sorsol()
    print(f"{x+1}. hét nyerőszámai: {számlista}")

def sorsol(hány = int(6), mettől = int(1), meddig = int(90)) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
        lista.sort()
    return lista
    
for x in range(52):
    számlista = sorsol()
    számlista2 = sorsol()
    print(f"{x+1}. hét nyerőszámai: {számlista} {számlista2}")

