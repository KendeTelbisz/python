import random

számlista = []

for x in range(100): 
    számlista.append(random.randint(2000, 3000))

számlista.sort()
print(f"Elemek növekvő sorrendben:{számlista}")
print("-  -  -") #alább a növekvő lista rendezését elveszíted

számlista.sort(reverse=True)
print(f"Elemek csökkenő sorrendben:{számlista}")

'''
for x in számlista:
    print(x)
'''
#lista bejárása while ciklussal
index = 0
while index < len (számlista):
    print(f"{index}. elem:{számlista[index]}")
    index+=1


index = 0 
while index < len(számlista):
    print(f"{index+1}. elem: {számlista[index]/17:.2f}")
    index += 1    