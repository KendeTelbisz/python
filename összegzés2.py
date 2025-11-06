számlista = True
    
while számlista >= -5 or számlista <= 5: 
    számlista = int(input("írjon be egész számokat a -5;5 intervallumon! a bekérés akkor fejeződik be ha egy az intervallumon kívüli számot ad  meg "))
    if számlista < -5 or számlista > 5:
        print(f"Összegezvén: {sum(számlista)}")


