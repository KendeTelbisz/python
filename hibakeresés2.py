try:
    lista = [1, 2, 3]
    print(lista[5])        #IndexError
    print(10/0)            #ZeroDivisionError

except(IndexError, ZeroDivisionError) as hiba:
    print("Hiba történt:", hiba)