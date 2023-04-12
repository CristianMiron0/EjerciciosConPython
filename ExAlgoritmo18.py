# Codigo que determine si una cadena de texto es un anagrama de otra cadena de texto

# Entrada
def ordenar(cadena):
    lista = list(cadena.lower())
    lista_ordenada = sorted(lista)
    cadena_ordenada = "".join(lista_ordenada)
    return cadena_ordenada

# Proceso
def es_anagrama(cadena1, cadena2):
    cadena1_ordenada = ordenar(cadena1)
    cadena2_ordenada = ordenar(cadena2)
    if cadena1_ordenada == cadena2_ordenada:
        return "Las cadenas son anagramas."
    else:
        return "Las cadenas no son anagramas."

# Salida
cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")
print(es_anagrama(cadena1, cadena2))
