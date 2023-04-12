# Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30").
 ## La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.

while True:
    timeStr = input("Enter a time in hh:mm format: ")
    try:
        hours, minutes = timeStr.split(":")
        hours = int(hours)
        minutes = int(minutes)
        
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            print("Invalid input. Please enter a valid time in hh:mm format.")
            continue
        break
    except ValueError:
        print("Value error. Please enter a valid time in hh:mm format.")
        continue

if hours < 12 and hours >= 1:
    period = "AM"
else:
    period = "PM"

if period == "PM" and hours != 12:
    hours -= 12

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)

print(f"{hours}:{minutes}")
