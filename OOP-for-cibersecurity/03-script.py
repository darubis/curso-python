import bcrypt
import time  # Necesario para manejar el tiempo de bloqueo

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password_hash = self.hash_password(password)
        self.intentos_fallidos = 0  # Contador de intentos de acceso fallidos
        self.bloqueado_hasta = None  # Almacena la hora de desbloqueo si se bloquea

    def hash_password(self, password):
        """Cifra la contraseña usando bcrypt con un salt aleatorio"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def verificar_password(self, password):
        """Verifica si la contraseña ingresada es correcta"""
        if self.bloqueado_hasta and time.time() < self.bloqueado_hasta:
            print(f"❌ Usuario bloqueado. Intenta nuevamente después de {self.bloqueado_hasta - time.time():.2f} segundos.")
            return False

        if bcrypt.checkpw(password.encode(), self.password_hash):
            print("✅ Acceso concedido")
            self.intentos_fallidos = 0  # Reinicia el contador si el acceso es exitoso
            return True
        else:
            self.intentos_fallidos += 1
            print(f"❌ Contraseña incorrecta. Intento {self.intentos_fallidos}/3")

            if self.intentos_fallidos >= 3:
                self.bloqueado_hasta = time.time() + 30  # Bloquea por 30 segundos
                print("⛔ Usuario bloqueado temporalmente por demasiados intentos fallidos.")
            return False

    def cambiar_contrasena(self, current_password, new_password):
        """Permite cambiar la contraseña de forma segura"""
        if self.verificar_password(current_password):
            self.password_hash = self.hash_password(new_password)
            print("✅ Contraseña cambiada exitosamente.")
        else:
            print("❌ No se pudo cambiar la contraseña.")
            
# 🔍 Prueba del sistema
usuario1 = Usuario("Alice", "segura123")

# Intentos de acceso
usuario1.verificar_password("incorrecta")  # 1er intento fallido
usuario1.verificar_password("incorrecta")  # 2do intento fallido
usuario1.verificar_password("incorrecta")  # 3er intento -> Bloquea usuario
usuario1.verificar_password("segura123")   # No permite acceso porque está bloqueado

# Esperamos 30 segundos (para pruebas, puedes reducir este tiempo)
time.sleep(30)

# Ahora el usuario puede intentar nuevamente
usuario1.verificar_password("segura123")  # Acceso exitoso