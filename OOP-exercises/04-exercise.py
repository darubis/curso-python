# Ejercicio 1: Generador de Hashes con Salting

# Objetivo: Implementar un sistema que almacene contraseñas usando bcrypt con salting y permita verificarlas.
# Requisitos:

#     Crear una clase SecurePasswordManager con:
#         Un método hash_password(password) que devuelva el hash de la contraseña usando bcrypt.
#         Un método check_password(password, hashed_password) que compare una contraseña con su hash almacenado.
#     Permitir almacenar múltiples contraseñas en un diccionario (usuarios = {}) con nombre de usuario como clave.
#     Agregar un método register_user(username, password) para registrar usuarios con su contraseña hasheada.
#     # Agregar un método authenticate(username, password) que verifique si la contraseña ingresada es correcta.

import bcrypt

class SecurePasswordManager:

    def __init__(self, password):
        self.password_hash = self.hash_password(password)
        self.usuarios = {}

    # devolver contrasena encriptada con bycrypt 
    def hash_password(self, password):
        salt = bcrypt.gensalt()  # Genera un "salt" aleatorio
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password

    def check_password(self, password):
        if bcrypt.checkpw(password.encode(), self.password_hash):
            print("✅ Contraseña correcta")
        else:
            print("❌ Contraseña incorrecta")

    def register_user(self, username, password):
        salt = bcrypt.gensalt()
        self.usuarios[username] = bcrypt.hashpw(password, salt)

    def authenticate(self, username, password):
        if username in self.usuarios.keys() and self.check_password(password):
            pass

