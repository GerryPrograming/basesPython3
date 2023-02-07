
import time # la hora como numero real de segundos

print(time.time()) # numero de segundos que han transcurrido de 1980

tiempo = time.time()

# convertir a una estructura mas legible 
print(time.localtime(tiempo))

tiempo = time.localtime(tiempo)

# obtener el año en el que estamos actualmente
print(tiempo.tm_year)

# representar el tiempo en formato cadena
print(time.asctime())

# cambiar el formato determinado
print(time.strftime('%d/%m/%Y %H:%M:5S'))

from datetime import datetime # mejora del anterior

print(datetime.now()) # objeto de la hora actual

print(datetime.now().day,datetime.now().month,datetime.now().year) # obtencion de dia mes y año

from datetime import date, datetime, time, timedelta

hora1 = time(10,5,0)
hora2 = time(23,15,0)
# realizar comparaciones de horas 
print(hora1 > hora2)

fecha1 =date.today() # fecha acual que sera sumada una fecha despues
fecha2 = fecha1 + timedelta(days=2)
print(fecha2)

print(fecha1.strftime('%d/%m/%Y')) # APLICANDO UN FORMATO

import calendar

anio = date.today().year
print(anio) # año actual

mes = date.today().month
print(mes) # mes actual

calendario_mes = calendar.month(anio,mes)
print(calendario_mes) # genera el calendario para imprimir el mes actual

# ver todos el calendario del año actual
print(calendar.TextCalendar(calendar.MONDAY).formatyear(2023,1,1,1,4))