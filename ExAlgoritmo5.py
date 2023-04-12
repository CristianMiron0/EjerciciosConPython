# A partir de una lista de números, determine cuál es el más grande y cuál es el más pequeño

# Entrada
listaDeNumeros = [1, 2, 5, 7, 8, 10]
mayor = listaDeNumeros[0]
menor = listaDeNumeros[0]

# Proceso
for numero in listaDeNumeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    
# Salida
print("Numero mayor:", mayor)
print("Numero menor:", menor)