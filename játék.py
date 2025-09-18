import random

játékos_1_dobás = random.randint(1, 6)
játékos_2_dobás = random.randint(1, 6)

print(f"Első játékos: {játékos_1_dobás}\n"
      f"Második játékos: {játékos_2_dobás}")                 

if játékos_1_dobás > játékos_2_dobás:
    print("Az első játékos nyert!")
elif játékos_1_dobás == játékos_2_dobás:    
    print("Döntetlen!")
else:    
    print("A második játékos nyert!")    