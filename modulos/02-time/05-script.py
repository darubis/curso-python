import time

inicio = time.time()  # Guardamos el tiempo de inicio

# Simulamos una tarea que toma tiempo
for i in range(1000000):
    pass

fin = time.time()  # Guardamos el tiempo de finalización

print(f"El código tomó {fin - inicio:.4f} segundos en ejecutarse")