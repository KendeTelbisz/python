try:
    x = int(input("Adj meg egy számot: "))
    print("A szám duplája:", x * 2)
except ValueError:
    print("Hibás bevitel! Számot kell megadni!")
