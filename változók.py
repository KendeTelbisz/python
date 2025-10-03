szám_1 = int(input("Kérek egy számot:"))
szám_2 = int(input("Kérek egy másik számot:"))

össz = szám_1 + szám_2
kiv = szám_1 - szám_2
szor = szám_1 * szám_2
oszt = szám_1 / szám_2
mar = szám_1 % szám_2

print(f"A két szám összege: {össz} \n"
      f"A két szám különbsége: {kiv}\n"
      f"A két szám szorzata: {szor}\n"
      f"A két szám hányadosa: {oszt:.2f}\n"
      f"Az osztás maradéka: {mar}\n")