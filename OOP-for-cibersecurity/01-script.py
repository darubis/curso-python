# Ejercicio

# Mejora el sistema agregando:

#     Un método para cambiar la contraseña de manera segura.
#     Protección contra ataques de fuerza bruta (por ejemplo, limitando intentos).


import hashlib

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password_hash = self.hash_password(password)
        self.intentos_fallidos = 0  # Controla intentos de cambio de contraseña

    def hash_password(self, password):
        """Cifra la contraseña usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verificar_password(self, password):
        """Verifica si la contraseña ingresada es correcta"""
        return self.password_hash == self.hash_password(password)

    def cambiar_contrasena(self, current_password, new_password):
        """Permite cambiar la contraseña con un límite de intentos"""
        MAX_INTENTOS = 3

        if self.intentos_fallidos >= MAX_INTENTOS:
            print("Demasiados intentos fallidos. Contacte al administrador.")
            return
        
        if self.verificar_password(current_password):
            self.password = self.hash_password(new_password)
            self.intentos_fallidos = 0  # Restablece intentos tras éxito
            print("Contraseña cambiada exitosamente.")
        else:
            self.intentos_fallidos += 1
            print(f"Las contraseñas no coinciden. Intento {self.intentos_fallidos}/{MAX_INTENTOS}")
            
            if self.intentos_fallidos >= MAX_INTENTOS:
                print("Demasiados intentos fallidos. Se bloqueó el cambio de contraseña.")

# Prueba del sistema
usuario1 = Usuario("Alice", "segura123")
print("Hash almacenado:", usuario1.password_hash)

# Intento de acceso
password_ingresada = "segura123"
if usuario1.verificar_password(password_ingresada):
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Intento de cambio de contraseña
usuario1.cambiar_contrasena("incorrecta", "nueva123")  # Falla
usuario1.cambiar_contrasena("incorrecta", "nueva123")  # Falla
usuario1.cambiar_contrasena("incorrecta", "nueva123")  # Bloquea
usuario1.cambiar_contrasena("segura123", "nueva123")   # No permite más cambios