# 🔒 Hashing Seguro de Contraseñas con bcrypt en Python

# Hasta ahora, hemos usado SHA-256 para almacenar contraseñas, pero tiene una debilidad importante:
# ✅ Es rápido, lo que lo hace vulnerable a ataques de fuerza bruta y diccionario con hardware especializado (como GPU o ASICs).

# 💡 Solución: Usar bcrypt, que es un algoritmo de hashing más seguro porque:

#     Es lento de propósito: Hace que los ataques de fuerza bruta sean mucho más difíciles.
#     Usa "salts" automáticamente: Un salt es un dato aleatorio añadido antes de cifrar la contraseña, evitando ataques de diccionario y tablas rainbow.

# 🚀 Ejemplo 1: Cómo Funciona bcrypt en Python


# Ejemplo 1: Cómo Funciona bcrypt en Python

import bcrypt

# Crear una contraseña segura
password = "segura123".encode()  # bcrypt requiere que las contraseñas estén en bytes
salt = bcrypt.gensalt()  # Genera un "salt" aleatorio
hashed_password = bcrypt.hashpw(password, salt)  # Genera el hash de la contraseña

print("Salt generado:", salt)
print("Contraseña hasheada:", hashed_password)

# Verificar una contraseña ingresada
password_ingresada = "segura123".encode()  # Convertimos a bytes
if bcrypt.checkpw(password_ingresada, hashed_password):
    print("✅ Contraseña correcta")
else:
    print("❌ Contraseña incorrecta")