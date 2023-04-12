# Calcular la lerra del DNI Espanol

import re

while True:
    dni = input("Please type your DNI number:")
    if re.match(pattern="^/d{8}$", string=dni):
        letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
        resto = int(dni) % 23
        resultado = f"The letter for your dni {dni} is {letrasDNI[resto]}"
        break
    elif dni == "":
        resultado = "Sin DNI"
        break
    else:
        resultado = "The number is not valid"
        print(resultado)

print(resultado)