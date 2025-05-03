#!/usr/bin/env python3

# Este script utiliza generadores en Python.

# Definición de un generador. 
# Los generadores son funciones que retornan un valor con 'yield' y mantienen su estado para continuar la ejecución en la próxima invocación.
def my_generator():
    yield 1  # 'yield' pausa la función y devuelve el valor 1
    yield 2  # 'yield' pausa la función y devuelve el valor 2
    yield 3  # 'yield' pausa la función y devuelve el valor 3

# Iteramos sobre el generador. Cada vez que se llama al generador, se ejecuta hasta el próximo 'yield'.
for value in my_generator():
    print(value)  # Imprime cada valor que el generador produce