____
Un generador en Python es un tipo especial de función que permite iterar sobre una secuencia de valores de manera más eficiente en términos de memoria y procesamiento. A diferencia de una lista, que almacena todos sus elementos en memoria, un generador produce (o "genera") cada elemento sobre la marcha, cuando es necesario.
Cómo funcionan los generadores

Un generador se crea utilizando una función que contiene la palabra clave yield en lugar de return. Cuando la función se llama, en lugar de ejecutarse completamente y devolver un valor, devuelve un iterador que produce los valores uno a uno, cada vez que se llama a next() sobre él.
Ejemplo simple de un generador

```
def contador(maximo):
    contador_actual = 1
    while contador_actual <= maximo:
        yield contador_actual
        contador_actual += 1
```

En este ejemplo:

1. **Definición**: La función `contador` es un generador que cuenta desde 1 hasta el número `maximo`.
2. **`yield`**: Cada vez que la función alcanza `yield`, detiene su ejecución y "devuelve" el valor de `contador_actual` al iterador.
3. **Retoma**: La próxima vez que se invoque el generador (por ejemplo, con `next()`), retoma la ejecución justo después del `yield`, incrementa `contador_actual` y vuelve a ceder el control al iterador.

### Usando el generador

```
mi_contador = contador(3)

print(next(mi_contador))  # Salida: 1
print(next(mi_contador))  # Salida: 2
print(next(mi_contador))  # Salida: 3
# Si intentas llamar a next() otra vez, lanzará un error StopIteration
```

### Ventajas de los generadores

1. **Eficiencia de memoria**: Como los generadores producen elementos sobre la marcha, no requieren almacenar todos los elementos en memoria.
    
2. **Eficiencia en tiempo de ejecución**: Puedes procesar elementos de grandes secuencias sin necesidad de esperar a que toda la secuencia sea generada y almacenada.
    

### Ejemplo práctico: Generador de números Fibonacci

```
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _ in range(10):
    print(next(fib))  # Imprime los primeros 10 números de Fibonacci
```

En este caso, el generador `fibonacci` genera una secuencia infinita de números de Fibonacci. Solo se calculan los números cuando se necesitan.

### Resumen

- Los generadores permiten crear secuencias de elementos de manera más eficiente en términos de memoria y procesamiento.
- Usan `yield` para devolver un valor y retener el estado de la función hasta la siguiente llamada.
- Son especialmente útiles para trabajar con secuencias grandes o infinitas, ya que no es necesario cargar todos los elementos en memoria al mismo tiempo.