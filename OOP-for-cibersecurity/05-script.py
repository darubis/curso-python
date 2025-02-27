import bcrypt
import sqlite3
import smtplib
import random
import time

class SistemaUsuarios:
    def __init__(self):
        """Inicializa la conexión a la base de datos y crea la tabla de usuarios"""
        self.conexion = sqlite3.connect("usuarios.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla de usuarios si no existe"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                nombre TEXT PRIMARY KEY,
                email TEXT,
                password_hash BLOB,
                pregunta TEXT,
                respuesta_hash BLOB
            )
        ''')
        self.conexion.commit()

    def registrar_usuario(self, nombre, email, password, pregunta, respuesta):
        """Registra un nuevo usuario en la base de datos"""
        if self.usuario_existe(nombre):
            print("❌ El usuario ya existe.")
            return

        password_hash = self.hash_password(password)
        respuesta_hash = self.hash_password(respuesta)

        self.cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?)", 
                            (nombre, email, password_hash, pregunta, respuesta_hash))
        self.conexion.commit()
        print("✅ Usuario registrado exitosamente.")

    def usuario_existe(self, nombre):
        """Verifica si el usuario ya existe en la base de datos"""
        self.cursor.execute("SELECT nombre FROM usuarios WHERE nombre = ?", (nombre,))
        return self.cursor.fetchone() is not None

    def hash_password(self, password):
        """Genera un hash seguro para la contraseña"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def verificar_usuario(self, nombre, password):
        """Verifica si el usuario y la contraseña son correctos"""
        self.cursor.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
        resultado = self.cursor.fetchone()

        if resultado and bcrypt.checkpw(password.encode(), resultado[0]):
            print("✅ Acceso concedido.")
            return True
        else:
            print("❌ Usuario o contraseña incorrectos.")
            return False

    def recuperar_por_pregunta(self, nombre):
        """Permite recuperar la contraseña con la pregunta de seguridad"""
        self.cursor.execute("SELECT pregunta, respuesta_hash FROM usuarios WHERE nombre = ?", (nombre,))
        resultado = self.cursor.fetchone()

        if not resultado:
            print("❌ Usuario no encontrado.")
            return

        pregunta, respuesta_hash = resultado
        respuesta_usuario = input(f"🔍 {pregunta}: ")

        if bcrypt.checkpw(respuesta_usuario.encode(), respuesta_hash):
            self.restablecer_contrasena(nombre)
        else:
            print("❌ Respuesta incorrecta.")

    def enviar_codigo_correo(self, email):
        """Envía un código de recuperación al correo del usuario"""
        codigo = str(random.randint(100000, 999999))
        remitente = "tucorreo@gmail.com"
        contraseña = "tu_contraseña"

        mensaje = f"Subject: Código de Recuperación\n\nTu código de recuperación es: {codigo}"

        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(remitente, contraseña)
            servidor.sendmail(remitente, email, mensaje)
            servidor.quit()
            print("📧 Código enviado al correo.")
            return codigo
        except Exception as e:
            print("❌ Error al enviar el correo:", e)
            return None

    def recuperar_por_correo(self, nombre):
        """Recupera la contraseña enviando un código al correo registrado"""
        self.cursor.execute("SELECT email FROM usuarios WHERE nombre = ?", (nombre,))
        resultado = self.cursor.fetchone()

        if not resultado:
            print("❌ Usuario no encontrado.")
            return

        email = resultado[0]
        codigo_generado = self.enviar_codigo_correo(email)

        if codigo_generado:
            codigo_ingresado = input("Introduce el código recibido en tu correo: ")
            if codigo_ingresado == codigo_generado:
                self.restablecer_contrasena(nombre)
            else:
                print("❌ Código incorrecto.")

    def restablecer_contrasena(self, nombre):
        """Permite al usuario restablecer su contraseña"""
        nueva_contrasena = input("Introduce tu nueva contraseña: ")
        nuevo_hash = self.hash_password(nueva_contrasena)
        self.cursor.execute("UPDATE usuarios SET password_hash = ? WHERE nombre = ?", (nuevo_hash, nombre))
        self.conexion.commit()
        print("✅ Contraseña restablecida con éxito.")

# 🔹 Interfaz de usuario
def menu():
    sistema = SistemaUsuarios()

    while True:
        print("\n🔐 MENÚ PRINCIPAL 🔐")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Recuperar contraseña")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de usuario: ")
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            pregunta = input("Pregunta de seguridad (Ej. ¿Cómo se llama tu primera mascota?): ")
            respuesta = input("Respuesta: ")
            sistema.registrar_usuario(nombre, email, password, pregunta, respuesta)

        elif opcion == "2":
            nombre = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            sistema.verificar_usuario(nombre, password)

        elif opcion == "3":
            print("\n🔄 Recuperación de Contraseña 🔄")
            print("1. Usar pregunta de seguridad")
            print("2. Usar código enviado al correo")
            metodo = input("Selecciona un método: ")

            nombre = input("Nombre de usuario: ")

            if metodo == "1":
                sistema.recuperar_por_pregunta(nombre)
            elif metodo == "2":
                sistema.recuperar_por_correo(nombre)
            else:
                print("❌ Opción no válida.")

        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar menú
menu()