# Codigo que calcule la media de la lista

# Entrada
lista = [2, 3, 5, 8, 10]

# Proceso
def media_lista(i):
    suma = 0
    contador = 0
    for numero in i:
        suma += numero
        contador += 1
    media = suma / contador
    return media

# Salida
print("La media de la lista es:", media_lista(lista))