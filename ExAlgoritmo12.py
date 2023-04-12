# Codigo que determine un numero entero si es primo o no

import math

# Entrada
numero = int(input("Type your number:"))

# Proceso
def divisores(n):
    result = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            result += 1
    return result

# Salida
div = divisores(numero)
if div == 1:
    print(f"{numero} is prime")
else:
    print(f"{numero} is not prime")