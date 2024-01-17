### Expresiones regulares ###

#? Es una mecanismo para comprobar si una cadena de texto tiene o no ciertos elementos

import re

my_string = 'Esta es la leccion numero 7: Expresiones Regulares'

my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros'

print(re.match('Esta es la leccion', my_string))
print(re.match('Esta es la leccion', my_other_string))
print(re.match('es la leccion', my_string)) #? 'None': el match empieza a buscar desde el inicio del string
