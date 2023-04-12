# Codigo que determine si una cadena de texto es un palindromo o no

# Entrada
cadena = input("Please type your phrase:")

# Proceso
cadena = cadena.lower().replace(" ", "")
reversa = cadena[::-1]
if cadena == reversa:
    resultado = "La cadena es un palindromo"
else:
    resultado = "La cadena no es un palindromo"

# Salida
print(resultado)