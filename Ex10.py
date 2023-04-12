# Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.
 ## La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

def filter_vowels(string_list):
    vowels = set('aeiouAEIOU')
    new_string_list = []
    for string in string_list:
        if any(i in vowels for i in string):
            new_string_list.append(string)
    return new_string_list

stringList = ["hello", "w0rld", "python", "programming"]
new_string_list = filter_vowels(stringList)

print(new_string_list)