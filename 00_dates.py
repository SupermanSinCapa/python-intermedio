### Dates ###

from datetime import datetime #? importamos dentro del modulo datetime el objeto datetime 

fecha_actual = datetime.now() #? Inicializamos guardamos en una variable el objeto construido con la fecha actual mediante now 

def print_date(date :datetime):
    print("----------Start------------")
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.timestamp())
    print("----------Stop-------------")
print_date(fecha_actual)

timestamp = fecha_actual.timestamp() #? Representacion unica de una fecha dada
print(timestamp)

year_2023 = datetime(2023, 1, 1) #! Obligatoriamente tienes que introducir al menos el año, el mes y el dia

print_date(year_2023)

from datetime import time #? time es diferente de datetime, se especializa en la hora

current_time = time(23, 12, 23) #* time debemos inicializar nosotros la hora que deseamos

print(f'Hora: {current_time.hour}')
print(f'Minutos: {current_time.minute}')
print(f'Segundos: {current_time.second}')

from datetime import date #? date es diferente de datetime, se especializa en la fecha

current_date = date(2023, 10, 29) #* Inicializamos nosotros la fecha que deseamos
#current_date = date.today() #* Guardamos la fecha actual

print(f'Dia: {current_date.day}')
print(f'Mes: {current_date.month}')
print(f'Año: {current_date.year}')

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = fecha_actual - year_2023
print(diff)

diff = current_date - year_2023.date()
print(diff)


from datetime import timedelta #? Se utiliza para trabajar con franjas de fechas con valores absolutos

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)


