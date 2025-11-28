tartalom = []
párosak = []
páratlanok = []

#try:
file = open("kimenet4.txt", "r")
tartalom = file.read()
 
for x in tartalom:
        if x % 2 == 0:
            párosak.append(x)
            with open('párosak.txt', 'w', encoding='utf-8') as adatfolyam:
                print('párosak', file=adatfolyam)
        else:
            páratlanok.append(x)
            with open('páratlanok.txt', 'w', encoding='utf-8') as adatfolyam: #lehet docx is a fájl kiterjesztése
                print('páratlanok', file=adatfolyam)

#except TypeError:
 #   print("A művelet nem hajtható végre!")