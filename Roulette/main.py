"""
Simula una ruleta de 37 numeros.
El 7 tiene mas probabilidad de salir.
Realiza 1000 tiradas y muestra cuantas 
veces sale el 7.
"""
import random

roulette = list(range(37))+[7]*10

counter = 0
for x in range(1000):
    if random.choice(roulette) == 7:
        counter += 1

print(counter)