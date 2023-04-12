# Codigo que determine si un numero es positivo, negativo o cero

# Entrada
numero = int(input("Numero:"))

# Proceso
def positivo_negativo(n):
    if n > 0:
        resultado = "El número es positivo"
    elif n < 0:
        resultado = "El número es negativo"
    else:
        resultado = "El número es cero"
    return resultado

# Salida
print(positivo_negativo(numero))