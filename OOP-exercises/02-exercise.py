# Ejercicio 2: Sistema de Gestión de Usuarios

# Descripción:
# Crea una clase User que represente un usuario en un sistema. Luego, implementa una clase AuthSystem que permita registrar usuarios y autenticarlos.
# Detalles:

#     La clase User debe tener atributos como username, password y role. Asegúrate de proteger la contraseña usando hashing (con hashlib).
#     La clase AuthSystem debe tener métodos para:
#         Registrar usuarios: Guardar usuarios en una lista.
#         Autenticar usuarios: Verificar si la contraseña ingresada coincide con la almacenada.
#         Mostrar usuarios (solo para el administrador).
#     La autenticación debe distinguir roles (por ejemplo: administrador y usuario regular).

# Restricciones:

#     Evita exponer contraseñas en texto plano.
#     Implementa control de acceso basado en roles.

import bcrypt

class User:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = self.encrypt_password(password)
        self.rol = rol
        self.failed_attempts = 0

    def encrypt_password(self, password):
        """Genera un hash seguro con bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def check_password(self, password):
        """Verifica si la contraseña es correcta"""
        return bcrypt.checkpw(password.encode(), self.password)

    def change_password(self, current_password, new_password):
        """Permite cambiar la contraseña si la actual es correcta"""
        MAX_ATTEMPTS = 3

        if self.failed_attempts >= MAX_ATTEMPTS:
            print("Demasiados intentos fallidos. Contacte al administrador.")
            return
        
        if self.check_password(current_password):
            self.password = self.encrypt_password(new_password)
            self.failed_attempts = 0
            print("Contraseña cambiada exitosamente.")
        else:
            self.failed_attempts += 1
            print(f"Las contraseñas no coinciden. Intento {self.failed_attempts}/{MAX_ATTEMPTS}")
            
            if self.failed_attempts >= MAX_ATTEMPTS:
                print("Demasiados intentos fallidos, cuenta bloqueada.")
    
    def __str__(self):
        """Evita mostrar la contraseña en el print del objeto"""
        return f"Usuario: {self.username}, Rol: {self.rol}"


class AuthSystem:
    def __init__(self):
        self.usuarios = []

    def add_user(self, new_user):
        """Agrega un usuario al sistema"""
        if isinstance(new_user, User):
            self.usuarios.append(new_user)
            print(f"\n[+] Usuario {new_user.username} agregado correctamente.")
        else:
            raise ValueError("El usuario ingresado no es válido.")

    def authenticate(self, username, password):
        """Verifica si un usuario puede iniciar sesión"""
        for user in self.usuarios:
            if user.username == username and user.check_password(password):
                print(f"\n[✔] Autenticación exitosa. Bienvenido, {user.username}.")
                return True
        print("\n[✘] Error: Usuario o contraseña incorrectos.")
        return False

    def show_users(self, requester):
        """Muestra los usuarios registrados (solo si el solicitante es admin)"""
        admin = next((u for u in self.usuarios if u.username == requester and u.rol == "admin"), None)

        if admin:
            print("\n[Usuarios Registrados]:")
            for user in self.usuarios:
                print(f"- {user}")
        else:
            print("\n[✘] Acceso denegado: Solo los administradores pueden ver la lista de usuarios.")


# Ejemplo de uso
if __name__ == "__main__":
    user1 = User("s4vitar", "12345", "admin")
    user2 = User("mario", "password", "invitado")

    system = AuthSystem()
    system.add_user(user1)
    system.add_user(user2)

    # Autenticación de usuario
    system.authenticate("mario", "password")

    # Mostrar usuarios (debe ser admin)
    system.show_users("s4vitar")

    # Intento de cambiar contraseña
    user1.change_password("12345", "nuevaClave123")