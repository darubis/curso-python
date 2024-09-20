#!/usr/bin/env python3

# Función tradicional que genera una lista de números pares hasta un límite.
def generar_pares(limite):
    num = 1  # Inicializamos el contador.

    mi_lista = []  # Creamos una lista vacía donde almacenaremos los pares.

    while num < limite:  # Mientras 'num' sea menor que el límite...
        mi_lista.append(num * 2)  # Añadimos el doble de 'num' (un número par) a la lista.
        num = num + 1  # Incrementamos 'num' para continuar la secuencia.

    return mi_lista  # Devolvemos la lista completa de números pares.

# Si descomentamos la siguiente línea, imprimirá la lista de números pares generados hasta el límite.
# print(generar_pares(10))

###################################################################################

# Generador que produce números pares de manera perezosa (lazy), generando uno a la vez.
def generar_pares(limite):
    num = 1  # Inicializamos el contador.

    while num < limite:  # Mientras 'num' sea menor que el límite...
        yield num * 2  # 'yield' devuelve el valor (número par) y pausa la ejecución del generador.
        num = num + 1  # Incrementamos 'num' para continuar la secuencia.

# Creamos una instancia del generador. No genera los valores inmediatamente, solo cuando se solicitan.
devuelve_pares = generar_pares(10)

# 'next' obtiene el siguiente valor generado. 
# La ejecución del generador continúa desde donde se pausó en el último 'yield'.
print(next(devuelve_pares))  # Imprime el primer par generado (2).

# Podemos tener más código entre llamadas a 'next', ya que el generador sigue en pausa.
print("Aqui podria haber mas codigo")

# Continuamos generando pares secuencialmente.
print(next(devuelve_pares))  # Imprime el siguiente par generado (4).
print(next(devuelve_pares))  # Imprime el siguiente par generado (6).
