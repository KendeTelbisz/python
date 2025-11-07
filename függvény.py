import random
számlista = []
kerekített_lista = []

for x in range(200):
    számlista.append(round(random.random()))

for x in számlista:
    kerekített_lista.append(round(x, 0))

print(kerekített_lista)

db = 0
for i in range(len(számlista) - 2):
    if számlista[i] == 1 and számlista[i+1] == 0 and számlista[i+2] == 1:
        db += 1

print(f"a 111 ennyiszer szerepel a listában:", db)
        
       
