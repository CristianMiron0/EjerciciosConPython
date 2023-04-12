# Codigo que determine si un numero es capicua o no

# Entrada
numero = int(input("Type:"))
numeroInvertido = 0
numeroOriginal = numero

# Proceso
while numero > 0:
    i = numero % 10
    numeroInvertido = numeroInvertido * 10 + i
    numero = int(numero / 10)

# Salida
if numeroOriginal == numeroInvertido:
    print("El numero es capicua")
else:
    print("El numero no es capicua")