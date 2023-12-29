### Listas Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)] #? Es un for dentro de corchetes ya que lo que quiero guardar es una lista, el elemento i representa cada elemento de la lista y lo voy insertando de 1 en 1
print(my_list)

my_list = [i + 1 for i in my_original_list] #? Le adiciono 1 a cada elemento de la lista antes de guardarlo
print(my_list)

my_list = [i *2 for i in my_original_list] #? multiplico por dos cada elemento y lo guardo
print(my_list)

my_list = [i * i for i in my_original_list] #? multiplico por el mismo elemento en cada iteracion y guardo los valores
print(my_list)

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in my_original_list] #? Le adiciono 5 a cada elemento de la lista original y lo inserto en la nueva
print(my_list)

