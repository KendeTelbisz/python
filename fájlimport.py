#szöveg beolvasása fájlból
with open('forras.txt', 'r', encoding='utf-8') as fajl:
    szoveg = fajl.read()

#trükk (felesleges karakterek eltávolítása)

#trükk - 2
#elválasztók listája
elvalasztok = [' ', '\n', ',', '.', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
for jel in elvalasztok:
    szoveg = szoveg.replace(jel, ' ')

szavak = szoveg.split(' ')

szoveg = szoveg.lower()

print("szavak száma:", len(szavak))

tisztitott = []

for szo in szavak:
    if szo != "":
        tisztitott.append(szo)

szavak = tisztitott

for x in tisztitott:
    print(x)

# "a" betűvel kezdődő szavak listája
a_betűs_szavak = []

for szó in szavak:
    if szó[0] == 'a':
        a_betűs_szavak.append(szó)

a_betűs_szavak.sort()
print(a_betűs_szavak)


török = []

for szó in szavak:
    if szó == 'török':
        török.append(szó)
print("török szó előfordulásai:", len(török))

b_betűs_szavak = []

for szó in szavak:
    if szó[0] == 'b':
        b_betűs_szavak.append(szó)

b_betűs_szavak.sort()
print(b_betűs_szavak)


c_betűs_szavak = []

for szó in szavak:
    if szó[0] == 'c':
        c_betűs_szavak.append(szó)

c_betűs_szavak.sort()
print(c_betűs_szavak)


d_betűs_szavak = []

for szó in szavak:
    if szó[0] == 'd':
        d_betűs_szavak.append(szó)

d_betűs_szavak.sort()
print(d_betűs_szavak)

#exportálás
with open('kimenet_egricsillagok.txt', 'w', encoding='utf-8') as célfájl:
    print(a_betűs_szavak, b_betűs_szavak, c_betűs_szavak, d_betűs_szavak, file=célfájl)
    



