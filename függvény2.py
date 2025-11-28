def lista_összeg() -> list:
    számlista = [1, 2, 3, 4, 5,]
    össz = 0
    for x in számlista:
        össz += x

def egyenlet(a: int, b: int, c = int(100)):
    return print(f"Az egyenlet eredménye: {(a*b)+(b*c)/2-765+1}")

print(f"Eredmény: {lista_összeg()}")