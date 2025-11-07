a = int(5) # szám tipusu
b = str("alma") # szöveg tipusu
c = bool(True)
d = 12

# az "=" az deklaráció (értékadás)

számlista = [5, 23, 17, 98, 2]
szöveglista = ["alma, körte, szilva", 1, 5, 6]

import random
sorsolt_szlista = []
gyümölcslista = ["alma", "körte", "szilva", "eper", "mangó", "paradicsom", "görögdinnye", "kiwi", "szőlő", "füge"]

# for x in range lista feltöltése
for x in range(100):
    sorsolt_szlista.append(random.randint(0, 9)) # 0 és 9 között sorsolok

print(f"Lista elemei{sorsolt_szlista}")

átalakított_lista = []

for x in sorsolt_szlista:
    if x == 0:
        átalakított_lista.append(gyümölcslista[0]) # ha az if igaz akkor elif nem fut le
    elif x == 1:
        átalakított_lista.append(gyümölcslista[1])
    elif x == 2:
        átalakított_lista.append(gyümölcslista[2])
    elif x == 3:
        átalakított_lista.append(gyümölcslista[3])
    elif x == 4:
        átalakított_lista.append(gyümölcslista[4])
    elif x == 5:
        átalakított_lista.append(gyümölcslista[5])
    elif x == 6:
        átalakított_lista.append(gyümölcslista[6])
    elif x == 7:
        átalakított_lista.append(gyümölcslista[7])
    elif x == 8:
        átalakított_lista.append(gyümölcslista[8])
    elif x == 9:
        átalakított_lista.append(gyümölcslista[9])

print(f"Lista elemeinek száma: {len(átalakított_lista)}")
print(átalakított_lista)

if "eper" in átalakított_lista: # ez egy bool vagy igen vagy nem
    print("Szerepel a listában!")
else:
    print("Nem szerepel a listában!")

eperszáma = 0 # az eper száma egy üres változó 
köteszáma = 0
szilvaszáma = 0



