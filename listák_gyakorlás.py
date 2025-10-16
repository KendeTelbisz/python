import random 

lista = []
pároslista = []
páratlanlista = []

for x in range (99):
    lista.append(random.randint(10, 99))


for x in lista:
    if x % 2 == 0:
        pároslista.append(x)
    else:
        páratlanlista.append(x)


print(lista)        

print(f"Elemek: {lista}\n"
      f"Az első szám:{lista[0]}\n"
      f"Az elemek száma: {len(lista)}\n"
      f"A legnagyobb elem: {max(lista)}\n"
      f"A legkisebb elem: {min(lista)}\n"
      f"Elemek összege: {sum(lista)}\n"
      f"Utolsó elem: {lista[len(lista)-1]}\n")


print(pároslista)

print(f"Elemek: {pároslista}\n"
      f"Az első szám:{pároslista[0]}\n"
      f"Az elemek száma: {len(pároslista)}\n"
      f"A legnagyobb elem: {max(pároslista)}\n"
      f"A legkisebb elem: {min(pároslista)}\n"
      f"Elemek összege: {sum(pároslista)}\n"
      f"Utolsó elem: {pároslista[len(pároslista)-1]}\n")


print(páratlanlista)

print(f"Elemek: {páratlanlista} \n" 
      f"Az első szám:{páratlanlista[0]}\n"
      f"Az elemek száma: {len(páratlanlista)}\n"
      f"A legnagyobb elem: {max(páratlanlista)}\n"
      f"A legkisebb elem: {min(páratlanlista)}\n"
      f"Elemek összege: {sum(páratlanlista)}\n"
      f"Utolsó elem: {páratlanlista[len(páratlanlista)-1]}\n")


print(f"\n ----------------------------------------------------"
      f"\n|        Lista        | Páros lista | Páratlan lista |" 
      f"\n ----------------------------------------------------"
      f"\n|Első elem: {lista[0]}        |     {pároslista[0]}      |     {páratlanlista[0]}         |" 
      f"\n ----------------------------------------------------"
      f"\n|Elemek száma: {len(lista)}     |     {len(pároslista)}      |     {len(páratlanlista)}         |"
      f"\n ----------------------------------------------------"
      f"\n|Legnagyobb elem: {max(lista)}  |     {max(pároslista)}      |     {max(páratlanlista)}         |"
      f"\n ----------------------------------------------------"
      f"\n|Legkisebb elem: {min(lista)}   |     {min(pároslista)}      |     {min(páratlanlista)}         |"
      f"\n ----------------------------------------------------"
      f"\n|Elemek összege: {sum(lista)} |     {sum(pároslista)}    |     {sum(páratlanlista)}       |"
      f"\n ----------------------------------------------------")