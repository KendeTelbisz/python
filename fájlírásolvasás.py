import random
számlista = []
páros = []
páratlan = []

for _ in range(1000):
    számlista.append(random.randint(10, 500))

kiirando = ";".join(map(str, számlista))  

with open('fájlírásolvasás.txt', 'w', encoding='utf-8') as adatfolyam:
    print(kiirando, file=adatfolyam)
  

with open('forrás2.txt', 'r', encoding='utf-8') as adatfolyam: 
    tartalom = adatfolyam.read()

for x in számlista:
    if x % 2 == 0:
        páros.append(x)
    else:
        páratlan.append(x)

páros.sort()
páratlan.sort()

kiirando_páros = ";".join(map(str, páros))
kiirando_páratlan = ";".join(map(str, páratlan))

with open('./páros.txt', 'w', encoding='utf-8') as adatfolyam:
    print(kiirando_páros, file=adatfolyam)
    print("A páros.txt elkészült!")

print("\n")

with open('./páratlan.txt', 'w', encoding='utf-8') as adatfolyam:
    print(kiirando_páratlan, file=adatfolyam)
    print("A páratlan.txt elkészült!")

