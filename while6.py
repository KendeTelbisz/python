import random
szöveglista = []

for x in range(100):
    index = random.randint(0, 9)
    if index == 0:
        szöveglista.append("alma")
    elif index == 1:
        szöveglista.append("szilva")
    elif index == 2:
        szöveglista.append("körte")
    elif index == 3:
        szöveglista.append("mangó")
    elif index == 4:
        szöveglista.append("őszibarack")