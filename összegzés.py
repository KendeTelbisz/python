import random
lista = []
pároslista = []

for x in range(5):
    lista.append(random.randint(1, 10))
print(lista)
print(f"összeg: {sum(lista)}")

for x in lista:
    if x % 2 == 0:
        pároslista.append(x)
        
print(pároslista)