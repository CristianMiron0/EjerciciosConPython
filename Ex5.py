# Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh").
 ## El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.

def phrase(string):
    reverseString = ""
    for i in range(len(string)-1, -1, -1):
        reverseString += string[i]
    return reverseString

userInput = input("Enter a string: ")
reverseString = phrase(userInput)

print("Reversed string:", reverseString)