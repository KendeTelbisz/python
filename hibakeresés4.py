try:
    file = open("adat.txt", "r")
    tartalom = file.read()
    print(tartalom)
except FileNotFoundError:
    print("A fájl nem található!")
finally:
    print("Program vége!")