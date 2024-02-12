### Expresiones regulares ###

#? Es una mecanismo para comprobar si una cadena de texto tiene o no ciertos elementos

import re

my_string = 'Esta es la leccion numero 7: Leccion llamada Expresiones Regulares'

my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros'

''' match '''  #? 'El match empieza a buscar desde el inicio del string y tiene que cohincidir

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
print(match.span()) #? span() es el rango. Te dice entre que lugares de la cadena se encuentra esta expresion regular, en el caso del ejemplo esta entre el caracter 0 y el 18.
span = match.span()
start, end = span
print(my_string[start:end])


match = re.match('Esta no es la leccion', my_other_string)
if match != None:
    print(match)
    span = match.span()
    start, end = span
    print(my_other_string[start:end])


''' search '''  #? El search busca la cadena que cohincida en cualquier lugar del string. El search solo muestra la primera vez que encuentra la cadena, en cambio el findall que se muestra a continuacion devuelve un arreglo con la cantidad deveces que encuentra la cadena

search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


''' findall '''  #? El search busca la cadena que cohincida en cualquier lugar del string. El search solo muestra la primera vez que encuentra la cadena, en cambio el findall que se muestra a continuacion devuelve un arreglo con la cantidad deveces que encuentra la cadena

findall = re.findall('leccion', my_string, re.I)
print(findall)

''' split '''  #? Busca un patron en el caso del ejemplo los dos puntos y divide la expresion cada vez que encuentra los dos puntos.

split = re.split(':', my_string)
print(split)

''' sub '''  #? Sustituye una expresion por otra, en el ejemplo cambio la palabra expresiones en mayuscula por expresiones en minuscula

sub = re.sub('Expresiones','expresiones', my_string)
print(sub)

print(re.sub('leccion|Leccion','LECCION', my_string)) #? Cambia leccion con minuscula y leccion con mayuscula por LECCION todo en mayuscula
