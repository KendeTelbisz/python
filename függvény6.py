import random
szöveglista = [] 

for x in range(2500):
    sorsolt = random.randint(0, 1)
    if sorsolt == 0:
        szöveglista.append("A")
    else:
        szöveglista.append("B")

print(szöveglista)

db = 0
for i in range(len(szöveglista) - 2):
    if szöveglista[i] == "A" and szöveglista[i+1] == "B" and szöveglista[i+2] == "B" and szöveglista[i+3] == "A":
        db += 1

print(f"az ABBA ennyiszer szerepel a listában:", db)