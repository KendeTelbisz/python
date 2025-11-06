a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy másik számot: "))
szó = str(input("Írj be egy szót: "))
if szó == "összeadás" or szó == "összeg":
    print(a + b)
if szó == "kivonás" or szó == "különbség":
    print(a - b)
if szó == "szorzás" or szó == "szorzat":
    print(a * b)
if szó == "osztás"  or szó == "hányados":
    print(a / b)
    print(a%b)     
