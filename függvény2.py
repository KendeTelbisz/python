def lista_összeg() -> list:
    számlista = [1, 2, 3, 4, 5,]
    össz = 0
    for x in számlista:
        össz += x

def egyenlet(a: int, b: int, c = int(100)):
    return(a*b)+(b*c)/2-765+1

print(f"Eredmény: {lista_összeg()}")
print(f"Az egyenlet eredménye: {egyenlet(11, 26, 200):.2f}")