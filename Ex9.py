# Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra.
 ## El programa debe utilizar un bucle `while` para buscar todas las ocurrencias de la palabra y reemplazarlas.

def replace_word(string, word, replacement_word):
    index = string.find(word)
    while index != -1:
        string = string[:index] + replacement_word + string[index + len(word):]
        index = string.find(word, index + len(replacement_word))
    return string

string = "The brown fox jumps over the lazy dog."
word = "fox"
replacement_word = "cat"
new_string = replace_word(string, word, replacement_word)

print(new_string)