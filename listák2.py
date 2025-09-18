import random

lista = []

for x in range(10000):#a zárójelben lévő számszor fog lefutni a ciklus - x bármi lehet
    lista.append(random.randint(1, 5000))

#print(lista) lista elemeinek kiírása egymás mellé

print("LISTA ELEMEI:")
for x in lista: # a bejárás az elem számától függ (annyiszor ismétlődik)
    if x <1000: # 3 számjeggyel rendelkező számok
        print(x)

print("\na 999 ennyiszer szerepel:")
for x in lista:
    if x == 999:
        print(x)
        