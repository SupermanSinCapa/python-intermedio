### Lambdas ###

#? Es una forma mucho mas simple de crear funciones, se utiliza mucho para crear funciones dentro de funciones

sum_two_values = lambda first_value, second_value: first_value + second_value
print (sum_two_values(2, 4))

multiply_values = lambda  first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))