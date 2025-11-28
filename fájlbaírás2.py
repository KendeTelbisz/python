import random
számlista = []

for _ in range(100):
    számlista.append(random.randint(1, 100))

számlista.sort()

with open('kimenet2.txt', 'w', encoding='utf-8') as adatfolyam:
    print(F"{számlista}", sep=", ")
    print(f"{számlista}", sep=", ", file=adatfolyam)