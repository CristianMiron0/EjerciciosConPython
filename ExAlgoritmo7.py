# Codigo que determine si es par o impar

# Entrada
numero = int(input("Please type your number:"))

# Proceso
def par_impar(n):
    if n % 2 == 0:
        resultado = ("El numero es par")
    else:
        resultado = ("El numero es impar")
    return resultado

# Salida
print(par_impar(numero))