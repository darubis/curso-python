import time

inicio = time.time()

# Simulamos una tarea que tarda 2 segundos
time.sleep(2)

fin = time.time()
tiempo_transcurrido = fin - inicio
print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")