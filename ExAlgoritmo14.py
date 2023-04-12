# Codigo que calcule la suma de todos los numeros pares de la lista

# Entrada
lista = [1, 10, 12, 5, 8, 3]
sumaPara = 0

# Proceso
for n in lista:
    if n % 2 == 0:
        sumaPara += n

# Salida
print("La suma de los numeros de la lista:",sumaPara)