# Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. 
 ## El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.

def filter_multiples_of_three(num_list):
    new_num_list = []
    for num in num_list:
        if num % 3 == 0:
            new_num_list.append(num)
    return new_num_list

numList = [1, 3, 4, 6, 7, 9, 12, 15, 18, 20, 21]
new_num_list = filter_multiples_of_three(numList)

print(new_num_list)
