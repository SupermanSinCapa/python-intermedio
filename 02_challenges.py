### Retos de programacion ###

"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizzbuzz():
    #my_list = list(range(1, 101))

    for element in range(1, 101):
        if element % 3 == 0 and element % 5 == 0:
            print('fizzbuzz')
        elif element % 3 == 0:
            print('fizz')
        elif element % 5 == 0:
            print('buzz')
        else:
            print(element)

fizzbuzz()

"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(first, second):
    if first.lower() == second.lower(): # Ponemos todas las letras en minisculas para que no haya diferencia entre mayusculas y minuscula, primero comparamos que no sea la misma palabra.
        return False
    return sorted(first.lower()) == sorted(second.lower()) # sorted() es una funcion para ordenar cadenas, arreglos etc

print(anagrama('amor', 'Maro'))


"""
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...

"""
def my_fibonacci():

    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

my_fibonacci()


"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

"""

def is_primo(numero):
    if numero < 2:
        return False
    
    for index in range(2, numero):
        if numero % index == 0:
            return False
    
    return True


def num_primo():
    for item in range(1, 101):
        if is_primo(item):
            print(item)

num_primo()

"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 ? Cuadrado A = a * a
 ? Rectangulo A = base * altura
 ? Triangulo A = sqrt(s(s-a)(s-b)(s-c)), s = (a+b+c)/2
"""
from math import sqrt

def area_poligono(lado1, lado2, lado3, lado4 = 0):
    if lado4 == 0:
        s = (lado1 + lado2 + lado3) / 2
        semi_perimetro = s*(s-lado1)*(s-lado2)*(s-lado3)
        area = sqrt(semi_perimetro)
        return print(f'El area del triangulo es {area}')
    
    elif lado1 == lado2 == lado3 == lado4:
        area = lado1 * lado2
        return print(f'El area del cuadrado es {area}')
    else:
        if lado1 != lado2:
            area = lado1 * lado2
            return print(f'El area del rectangulo es {area}')
        elif lado1 != lado3:
            area = lado1 * lado3
            return print(f'El area del rectangulo es {area}')
        
area_poligono(2, 2, 2, 2)
area_poligono(3, 4, 5)
area_poligono(5,5,4,4)

