#!/usr/bin/env python3

# Definimos una función generadora que genera la secuencia de Fibonacci hasta un límite.
def fibonacci(limit):
    a, b = 0, 1  # Inicializamos los dos primeros números de la secuencia de Fibonacci.
    while a < limit:  # Continuamos generando números hasta que 'a' sea mayor o igual al límite.
        yield a  # 'yield' devuelve el valor actual de 'a' y pausa la ejecución de la función.
        a, b = b, a + b  # Actualizamos 'a' y 'b'. 'a' toma el valor de 'b', y 'b' es la suma de los dos anteriores.

# Iteramos sobre los números generados por el generador Fibonacci hasta llegar al límite.
for num in fibonacci(10):  # Llamamos al generador con un límite de 10.
    print(num)  # Imprimimos cada número generado en la secuencia.