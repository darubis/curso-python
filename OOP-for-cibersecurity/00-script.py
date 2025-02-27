# Ejemplo 1: Gestión de Usuarios y Contraseñas

# Vamos a crear un sistema básico para gestionar usuarios y verificar contraseñas de manera segura.
# Objetivo:

#     Crear una clase Usuario con un método para almacenar la contraseña de forma segura (hash).
#     Verificar contraseñas sin almacenarlas en texto plano.


import hashlib

class User:
    def __init__(self, name, password):
        self.name = name
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        """Cifra la contraseña usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Verifica si la contraseña ingresada es correcta"""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

# Prueba del sistema
user1 = User("Alice", "segura123")
print("Hash almacenado:", user1.password_hash)

# Intento de acceso
password_ingresada = "segura123"
if user1.check_password(password_ingresada):
    print("Acceso concedido")
else:
    print("Acceso denegado")