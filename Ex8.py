# Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres.
 ## El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

def filter_string(listString):
    return [i for i in listString if len(i) > 5]

inputList = ["car", "banana", "milk", "watermelon", "orange", "laptop"]
outputList = filter_string(inputList)

print(outputList)
