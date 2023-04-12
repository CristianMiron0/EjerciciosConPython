# Codigo que genere un numero aleatorio entre 1 y 100, y le pida al usuario adivinarlo

import random

# Entrada
numeroAlea = random.randint(1, 100)
intento = 0

# Proceso
while True:
    numeroUser = int(input("Adivina el número (entre 1 y 100): "))
    intento += 1
    if numeroUser < numeroAlea:
        print("Es más grande. Prueba de nuevo.")
    elif numeroUser > numeroAlea:
        print("Es más pequeño. Prueba de nuevo.")
    else:
        print(f"Felicidades. Encontraste el número correcto en {intento} intentos.")
        break