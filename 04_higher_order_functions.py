### Funciones de orden superior ###

#? A funciones se le pueden pasar funciones por parametros y dentro de la funciones se puede utilizar varias funciones


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_values(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

#? En el ejemplo siguiente se ve como con la misma funcion podemos en dependencia de la funcion que le pasemos por parametro modificar el resultado final.
print(sum_two_values_and_add_values(5, 2, sum_one))
print(sum_two_values_and_add_values(5, 2, sum_five))


### Closures ###
#? Permite devolver funciones dentro de otras funciones. Funcion que define una funcion y retorna una funcion

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))


def sum_more(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_more(1)
print(add_closure(5))

print(sum_more(5)(1))

### Funciones de orden superior propias de Python ###

# Map #? Recorre todos los valores y ejecuta una funcion sobre ellos para modificar su valor
numbers = [2, 5, 10, 21, 3, 30]
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers))) #* Se puede sustituir la lambda por la funcion multiply_two

# Filter #? Recorre todos los valores y ejecuta una funcion que retorna true o false para saber como filtrar los valores del iterado.
def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(lambda number: number > 10, numbers)))#* Se puede sustituir la lambda por la funcion filter_greater_than_ten

#Reduce #? En vase a todos los elementos del iterable o la lista ha sido capaz de ir juntandolos en vase a nuestro criterio en este caso el criterio es la funcion sum_two_values
from functools import reduce

def sum_two_values(first, second):
    return first + second

print(reduce(sum_two_values, numbers))
print(reduce(lambda first, second: first + second, numbers))