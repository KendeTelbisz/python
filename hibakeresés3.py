try:
    a = int("abc")
except ValueError:
    print("Nem alakítható számmá!")
except TypeError:
    print("Típushiba történt!")