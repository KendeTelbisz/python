with open('kimenet3.txt', 'r', encoding='utf-8') as adatfolyam: # ./mappanév/filenév, vagy ../mappanév/filenév <- megnézni ezt a kettőt
    tartalom = adatfolyam.read()

szamok = list(map(int, tartalom.split(";")))

#print(szamok)

for x in szamok:
    print(x)