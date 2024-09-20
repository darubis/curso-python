#!/usr/bin/env python3

# Ejemplo de iterador

my_list = [1,2,3,4]

# obtener el iterador
my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

###############################################################################

limit = 10

# range(start, top, step)
odd_iter = iter(range(0,limit+1,2))

for num in odd_iter:
    print(num)