# Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. 
 ## El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.

from datetime import datetime

# Entrada
while True:
    time = input("Please type the date in a dd/mm/aaaa format: ")
# Proceso
    try:
        timeObj = datetime.strptime(time, "%d/%m/%Y")
        newTime = timeObj.strftime("%Y-%m-%d")
        break
    except ValueError:
        print("Incorrect format. Please type a date with the following format: dd/mm/aaaa.")
# Salida
print("Your date in a new format is:", newTime)