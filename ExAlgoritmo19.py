# Codigo que elimine los numeros duplicados de la lista

# Entrada
lista = input("Introduce una lista de números separados por comas: ")
lista = lista.split(",")

# Proceso
resultados = []
for elemento in lista:
    if elemento not in resultados:
        resultados.append(elemento)

# Salida
print("La lista sin números duplicados es:", resultados)