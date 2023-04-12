# Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.
 ## El programa debe utilizar un bucle `for` para sumar los números.

num = int(input("Enter an integer: "))
total = 0

for i in range(1, num+1):
    total += i

print("The sum of all numbers from 1 to", num, "is:", total)