szám_1 = int(input("Kérek egy számot:"))
szám_2 = int(input("Kérek egy másik számot:"))

össz = szám_1 + szám_2
kiv = szám_1 - szám_2
szor = szám_1 * szám_2
oszt = szám_1 / szám_2
mar = szám_1 % szám_2

print(f"A két szám összege: {össz:.2f} \n"
      f"A két szám különbsége: {kiv:.2f}\n"
      f"A két szám szorzata: {szor:.2f}\n"
      f"A két szám hányadosa: {oszt:.2f}\n"
      f"Az osztás maradéka: {mar:.2f}\n")
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
a = int(5)
b = int(12)
c = int(input("Kérek egy egész számot:"))
d = int(input("Kérek egy másik egész számot:"))

#print("Első érték:",a)
#print("Második érték:",b)

print(f"Első érték: {a}\n"
      f"Második érték: {b}")

print(f"A két szám összege: {c+d}\n\n"
      f"\t A két szám szorzata: {c*d}\n\n"
      f"A két szám különbsége: {c-d}\n\n"
      f"\t A két szám hányadosa: {c/d}\n\n"
      f"A maradék: {c%d}")