import time

# Obtener la fecha y hora local en forma estructurada
tiempo_struct = time.localtime()
print(f"Año: {tiempo_struct.tm_year}, Mes: {tiempo_struct.tm_mon}, Día: {tiempo_struct.tm_mday}")