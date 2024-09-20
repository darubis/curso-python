#!/usr/bin/env python3


add = lambda a,b: a + b
# print(add(10,4))

multiply = lambda a,b: a * b
# print(multiply(13,5))

# obtener el cuadrado de cada numero
numbers = range(11)
squares = list(map(lambda a: a**2, numbers))
print("Cuadrados: ", squares)

# pares 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares: ", even_numbers)
