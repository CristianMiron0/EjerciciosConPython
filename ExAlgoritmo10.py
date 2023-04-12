# Codigo que ordene la lista alfabeticamente

# Entrada
listaNombres = ["Cristian", "Maria", "Jose", "Ana"]

# Proceso
for i in range(len(listaNombres)):
    for j in range(len(listaNombres) - 1 - i):
        if listaNombres[j] > listaNombres[j+1]:
            listaNombres[j], listaNombres[j+1] = listaNombres[j+1], listaNombres[j]

# Salida
print(listaNombres)