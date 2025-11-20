def összeg(a:int, b:int) -> int: #függvény (amikor az értékkel mnég akarok dolgozni)
    return a +b 

def összeg2(a:int, b:int) -> int: #alprogram (amikor csak kiíratok)
    össz = a + b
    print(f"A két szám összege máshogy: {össz}")

def összegzés(szám1: int, szám2: int, szám3 = int(100), szám4 = int(200)) -> int:
    eredmény = szám1 * szám2 + (szám3 * szám4) / szám4 +(szám4 + szám1)
    print(f"Az eredmény: {összeg(45,12)}")
print(f"A két szám összege: {összeg(45, 12)}")
összeg2(45, 12)

összegzés(34,12)

összegzés(845, 456, 123, 123)