import random
import math
import csv

def számlista() -> list:
    lista = []
    for _ in range(5):
        lista.append(random.randint(1, 99))
    lista
    return lista

for x in range(52): #52szer tőti fel a lottószámokot, kiírja majd felűlírja
    ötöslottószámok = számlista()
    print(f"{x+1}. hét nyerőszámai (5ös lottó): {ötöslottószámok}")

print("\n---------------------------------------------------------------------------------\n")

def számlista2() -> list:
    lista2 = []
    for _ in range(6):
        lista2.append(random.randint(1, 45))
    lista2
    return lista2

for x in range(52): #52szer tőti fel a lottószámokot, kiírja majd felűlírja
    hatoslottószámok = számlista2()
    hatoslottószámok2 = számlista2()
    print(f"{x+1}. hét nyerőszámai (6os lottó): {hatoslottószámok} {hatoslottószámok2}")