termékek = [] #lista létrehozása

#open - fájl megnyitása az 'r' kapcsolóval utf-8 kódolással
#as forrásfájl az adatfolyam neve 
#ezzel beolvassa soronként a fájlt és eltárolja
with open('áruház.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl: #ez és a következő sor 3 sor csak egyszer fut le, ezután pontosan annyiszor újra lefutni amennnyi sor van
        adatok = sor.strip().split(',')# vessző mentén darabokra szedi a sort, strip parancs szöveges függvény = eltünteti előről és hátulról a felesleges szóközöket, split szöveges függvény = megadott karakter mentén darabolt
        termék = {'termeknev': adatok[0], 'egysegar': int(adatok[1]), 'raktarkeszlet': int(adatok[2]), 'kategoria': adatok[3]}
        termékek.append(termék)# kulcs-érték párok hozzáadása listához

print(f'{termékek=}',end="\n\n")
print(f"{termékek[:5]}")