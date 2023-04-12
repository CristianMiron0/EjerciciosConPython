# Calcula el área y perímetro de un círculo dado su radio

# Entrada
radioDelCirculo = float(input("Radio del circulo:"))

# Proceso
pi = 3.14159
area = pi * radioDelCirculo**2
perimetro = 2 * pi * radioDelCirculo

# Salida
print("Area:", area)
print("Perimetro:", perimetro)