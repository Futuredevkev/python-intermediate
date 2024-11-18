## Dates ## 

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now() # Esta es la fecha actual

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() # Esto es la fecha en timestamp, que es el número de segundos que han pasado desde el 1 de enero de 1970
print(timestamp)


year_2025 = datetime(2025, 1, 1) # creamos un objeto completo de datetime con la fecha 1 de enero de 2025

def print_date(date): # creamos una función que imprime la fecha
  print(date.year)
  print(date.month)
  print(date.day)

print_date(year_2025)

current_time = time(21, 6, 0) # creamos un objeto time con la hora 21:06

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today() # el date today nos devuelve la fecha actual 

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 1, 1) # creamos un objeto date con la fecha 1 de enero de 2025

print(current_date.year)
print(current_date.month)
print(current_date.day)


# Diferencias entre fechas solo se pueden hacer si el tipo de dato es igual
diff = year_2025 - now # creamos una diferencia entre la fecha 1 de enero de 2025 y la fecha actual
print(diff)

diff = year_2025.date() - current_date 
print(diff)


# nos vale para operar y trabajar con diferencias de fechas, esto sirve como para calcular fechas futuras, servicios de membresia

start_time_delta = timedelta(200, 100, 100, weeks= 10)
end_time_delta = timedelta(200, 100, 100, weeks= 20)

print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)

