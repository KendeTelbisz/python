#szétválogatás alaptétele
#véletlenszám modul meghívása
import random

#üres listák létrehozása
számlista = []
pároslista = []
páratlanlista = []

#számlista feltöltése elemekkel

for x in range(100):
    számlista.append(random.randint(5000, 6000))

#szétválogatás - lista bejárása
for x in számlista:
    if x % 2 == 0:
        pároslista.append(x)
    else:
        páratlanlista.append(x)

print(pároslista)        
print(páratlanlista)
    