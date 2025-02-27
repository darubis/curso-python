import bcrypt
import sqlite3
import time

class Usuario:
    def __init__(self, nombre, password, pregunta, respuesta):
        """Crea un nuevo usuario y lo guarda en la base de datos"""
        self.conexion = sqlite3.connect("usuarios.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

        self.nombre = nombre
        self.password_hash = self.hash_password(password)
        self.pregunta = pregunta
        self.respuesta_hash = self.hash_password(respuesta)

        if not self.usuario_existe():
            self.guardar_usuario()

    def crear_tabla(self):
        """Crea la tabla de usuarios si no existe"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                nombre TEXT PRIMARY KEY,
                password_hash BLOB,
                pregunta TEXT,
                respuesta_hash BLOB
            )
        ''')
        self.conexion.commit()

    def usuario_existe(self):
        """Verifica si el usuario ya existe en la base de datos"""
        self.cursor.execute("SELECT nombre FROM usuarios WHERE nombre = ?", (self.nombre,))
        return self.cursor.fetchone() is not None

    def guardar_usuario(self):
        """Guarda el usuario en la base de datos"""
        self.cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", 
                            (self.nombre, self.password_hash, self.pregunta, self.respuesta_hash))
        self.conexion.commit()

    def hash_password(self, password):
        """Hashea la contraseña usando bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def verificar_password(self, password):
        """Verifica la contraseña"""
        self.cursor.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (self.nombre,))
        resultado = self.cursor.fetchone()

        if resultado and bcrypt.checkpw(password.encode(), resultado[0]):
            print("✅ Acceso concedido")
            return True
        else:
            print("❌ Contraseña incorrecta")
            return False

    def recuperar_contrasena(self, respuesta):
        """Verifica la respuesta de seguridad y permite resetear la contraseña"""
        self.cursor.execute("SELECT respuesta_hash FROM usuarios WHERE nombre = ?", (self.nombre,))
        resultado = self.cursor.fetchone()

        if resultado and bcrypt.checkpw(respuesta.encode(), resultado[0]):
            nueva_contra = input("Introduce tu nueva contraseña: ")
            nuevo_hash = self.hash_password(nueva_contra)
            self.cursor.execute("UPDATE usuarios SET password_hash = ? WHERE nombre = ?", (nuevo_hash, self.nombre))
            self.conexion.commit()
            print("✅ Contraseña restablecida con éxito")
        else:
            print("❌ Respuesta incorrecta")

# 🔍 Prueba del sistema
usuario1 = Usuario("Alice", "segura123", "¿Cómo se llama tu primera mascota?", "firulais")
usuario1.verificar_password("incorrecta")
usuario1.verificar_password("segura123")
usuario1.recuperar_contrasena("firulais")