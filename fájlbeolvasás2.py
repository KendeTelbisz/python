with open('forrás2.txt', 'r', encoding='utf-8') as adatfolyam: # ./mappanév/filenév, vagy ../mappanév/filenév <- megnézni ezt a kettőt
    tartalom = adatfolyam.read()

szöveglista = list(map(str, tartalom.strip().split(" ")))

szöveglista = [szó.strip(".,?!") for szó in szöveglista]
szöveglista = [szó.rstrip(".,?!") for szó in szöveglista] # rear strip, csak a végéről törli

for szó in szöveglista:
    print(szó)

#hány szó van a forrásban pontatlanul
print(f"Szavak száma a forrásban pontatlanul: {len(szöveglista)}")  

#hány szó van pontosan
elemszám = 0
for x in szöveglista:
    if x != " ":
        elemszám +=1

print(f"Szavak száma pontosan: {elemszám}")

#hány (a) betűvel kezdődő szó van
a_betűs_szavak = []
for szó in szöveglista:
    if szó[0] == "a" or szó == "A":
        a_betűs_szavak.append(szó)

print(f"(A) vagy (a) betűvel kezdődő szavak listája: {a_betűs_szavak}")

b_betűs_szavak = []
for szó in szöveglista:
    if szó[0] == "b" or szó == "B":
        b_betűs_szavak.append(szó)

print(f"(B) vagy (b) betűvel kezdődő szavak listája: {b_betűs_szavak}")

c_betűs_szavak = []
for szó in szöveglista:
    if szó[0] == "c" or szó == "C":
        c_betűs_szavak.append(szó)

print(f"(C) vagy (c) betűvel kezdődő szavak listája: {c_betűs_szavak}")        

d_betűs_szavak = []
for szó in szöveglista:
    if szó[0] == "d" or szó == "D":
        d_betűs_szavak.append(szó)

print(f"(D) vagy (d) betűvel kezdődő szavak listája: {d_betűs_szavak}")        

nre_végződő_szavak = []
for szó in szöveglista:
    if szó[len(szó)-1] == "n":
        nre_végződő_szavak.append(szó) 

print(f"Nre végződő szavak listája: {nre_végződő_szavak}")                               