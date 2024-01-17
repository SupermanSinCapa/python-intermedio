### Ficheros ###



#? Ficheros .txt 

import os

txt_file = open('./my_file.txt', 'w+')
txt_file.write('Mi nombre es Abel\nMi apellido es Tellechea\n37 annos\nMi lenguaje preferido es Python\nAunque tambien me gusta Kotlin')
#print(txt_file.read())
#print(txt_file.read(10)) #? el 10 es la cantidad de caracteres que queremos leer

#print(txt_file.readline())
#print(txt_file.readline())

#print(txt_file.readlines()) #? Leer todas las lineas y juntarlas en un listado
for line in txt_file.readlines():
    print(line)


txt_file.close()
#os.remove('./my_file.txt')


#? Ficheros .JSON

import json

json_file = open('./my_file.json', 'w+')

json_text = {
    'name': 'Abel',
    'surname': 'Tellechea',
    'age': 37,
    'language': ['Python', 'Swift', 'PHP'],
    'website': 'https://alldecorterrace.com'
}

json.dump(json_text, json_file, indent = 4) #? Para escribir un fichero JSON, parametros: 1- Un objeto (puede ser un diccionario), 2- El archivo json creado arriba con open(), 3- (Opcional) el indentado

json_file.close()


with open('./my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#? Para de un fichero json sacar la informacion y guardar en un diccionario toda esta info
json_dict = json.load(open('./my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])


#? Ficheros .CSV file 

import csv

csv_file = open('./my_file.csv', 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Abel', 'Tellechea', 37, 'Python', 'https://alldecorterrace.com'])

#csv_file.close()


#? Ficheros .XLSX file 
#import xlrd # Debemos instalar el modulo


#? Ficheros .XML file 

import xml