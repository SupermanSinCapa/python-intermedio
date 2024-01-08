### Tipos de errores ###

# SyntaxError #? Errores de sintaxis
# print 'Hola comunidad' #! Error
print('Hola comunidad')

# NameError #? Cuando no tenemos algo definido y lo llamamos
# print(name) #! Error
name = 'Abel'
print(name)

# IndexError #? Error de indice en una secuencia
my_list = ['Python', 'Swift', 'Kotlin', 'Dart']
# print(my_list[5]) #! Error
print(my_list[3])

# ModulenotfoundError #? Error cuando importamos un modulo que no existe
# import maths #! Error
import math

# AttributeError #? Error cuando un atributo no existe
# print(math.PI) #! Error
print(math.pi)

# KeyError #? Error cuando por ejemplo en un diccionario no colocamos bien en Key
my_dict = {'Nombre': 'Abel', 'Edad': 37}
# print(my_dict['Nombree']) #! Error
print(my_dict['Nombre'])

# TypeError #? Error cuando utilizamos por ejemplo en una lista una posicion que debe ser de tipo entero colocamos un string
# print(my_list['Nombre']) #! Error
print(my_list[1])

# ImportError #? Error cuando importamos de un modulo un apartado que no existe que no existe
# from math import pI #! Error
from math import pi

# ValueError #? Error cuando pasamos a una funcion un valor incorrecto
# my_int = int('10 annos') #! Error
my_int = int('10')
print(type(my_int))

# ZeroDivisionError #? Error cuando dividimos por cero
# print(4 / 0) #! Error
print(4 / 2) 
