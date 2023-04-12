# Codigo que calcule el factorial de un numero entero

# Entrada
numero = int(input("Numero entero:"))

# Proceso
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Salida
print("El factorial de {n} es {r}".format(n=numero, r= factorial(numero)))