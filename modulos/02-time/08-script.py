import time

def temporizador(segundos):
    while segundos:
        minutos, seg = divmod(segundos, 60)
        tiempo_formateado = f"{minutos:02}:{seg:02}"
        print(tiempo_formateado, end="\r")  # Sobreescribe la línea anterior
        time.sleep(1)
        segundos -= 1

    print("¡Tiempo terminado!")

# Ejecutar un temporizador de 10 segundos
temporizador(10)