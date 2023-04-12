# Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona.
 ## El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

import pytz
from datetime import datetime

timeZones = pytz.all_timezones
# Entrada
while True:
    userTimeZone = input("Please type your time zone (Exemple: Area/City):")
# Proceso
    try:
        timeZoneObj = pytz.timezone(userTimeZone)
        break
    except pytz.exceptions.UnknownTimeZoneError:
        print("This is not a valid time zone. Please type again.")

timeNow = datetime.now(timeZoneObj)
# Salida
print("Current time in {} is {}".format(userTimeZone, timeNow.time()))