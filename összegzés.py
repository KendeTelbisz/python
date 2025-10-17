#Összegzés algoritmusa

lista = [54, 12, 23, 67, 89, 12, 90]
tizenegyelosztahatóak = []

összeg = 0
for x in lista:
    összeg = összeg + x

print(f"A lista összegzése: {összeg}")

for x in lista:
    if x % 11 == 0:
        tizenegyelosztahatóak.append(x)

#átlagszámítás

jegyek = []

'''for x in range(5):
    jegyek.append(int(input("Add meg a jegyet: ")))

print(f"Az átlag: {sum(jegyek)/len(jegyek)}")
'''

'''for x in range(int(input("Hány jegyet szeretne megadni? "))):
    jegy = int(input("Adjon meg egy jeget! >>> "))
    if jegy < 1:
        print("Adjon meg egy nagyobb számot!")
    elif jegy > 5:
        print("Adjon meg egy kisebb számot!")
    else:
        jegyek.append(jegy)
'''

jegy = int(input("Adjon meg egy jeget! >>> "))

while jegy!= 0:
    jegy = int(input("Adjon meg egy jeget! >>> "))
    if jegy < 1:
        print("Adjon meg egy nagyobb számot!")
    elif jegy > 5:
        print("Adjon meg egy kisebb számot!")
    else:
        jegyek.append(jegy)

átlag = []
print(f"Az átlag: {sum(jegyek)/len(jegyek)}")

if 1 < átlag and 2 > átlag:
    print("Bukás!")
elif 2 <= átlag and 3 > átlag:
    print("Elégséges!")