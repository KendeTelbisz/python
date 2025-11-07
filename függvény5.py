#mintakeresés
import random
számlista = []

for x in range(2000):
    számlista.append(random.randint(1, 500))

print(számlista)

db = 0
for i in range(len(számlista) - 2):
    if számlista[x] == 7 and számlista[x+1] ==2 and számlista[x+2] ==1:
        db += 1

print(f"a 721 ennyiszer szerepel: {db}")