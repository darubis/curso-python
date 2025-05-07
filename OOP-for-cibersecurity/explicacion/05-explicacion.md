¡Excelente! Vamos a dividir la implementación en dos partes:

1️⃣ **Almacenar usuarios en una base de datos** usando `sqlite3` para que la información no se pierda cuando cerramos el programa.
2️⃣ **Implementar un sistema de recuperación de contraseña**, usando preguntas de seguridad y un código enviado por correo.

---

## **1️⃣ Guardando Usuarios en una Base de Datos (`SQLite`)**

### 📌 **Objetivo**: En lugar de almacenar los usuarios en memoria, guardaremos su información en una base de datos.

### 🔹 **Instalación y Configuración**

Python ya incluye `sqlite3`, por lo que no necesitas instalar nada.

### 🔹 **Código Mejorado con Base de Datos**

```python
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
```

---

## **📌 Explicación de la Implementación**

1. **Guardamos los usuarios en SQLite** en la tabla `usuarios`.
2. **Hasheamos la respuesta de seguridad** con `bcrypt` para mayor protección.
3. **Verificamos la respuesta de seguridad** antes de permitir cambiar la contraseña.

---

## **2️⃣ Recuperación de Contraseña por Código de Verificación (Correo)**

### 📌 **Objetivo**: Enviar un código único al correo del usuario para verificar su identidad.

### 🔹 **Instalar la Librería `smtplib`**

Python ya incluye `smtplib`, pero necesitas activar el acceso a aplicaciones menos seguras en tu cuenta de Gmail o usar un correo específico para pruebas.

### 🔹 **Código Mejorado**

```python
import smtplib
import random

class RecuperacionCorreo:
    def __init__(self, email):
        self.email = email
        self.codigo = str(random.randint(100000, 999999))  # Código de 6 dígitos

    def enviar_codigo(self):
        """Envía un código de recuperación al correo del usuario"""
        remitente = "tucorreo@gmail.com"
        contraseña = "tu_contraseña"

        mensaje = f"Subject: Código de Recuperación\n\nTu código de recuperación es: {self.codigo}"

        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(remitente, contraseña)
            servidor.sendmail(remitente, self.email, mensaje)
            servidor.quit()
            print("📧 Código enviado al correo")
        except Exception as e:
            print("❌ Error al enviar el correo:", e)

    def verificar_codigo(self, codigo_ingresado):
        """Verifica si el código ingresado es correcto"""
        if codigo_ingresado == self.codigo:
            print("✅ Código correcto. Puedes restablecer tu contraseña.")
            return True
        else:
            print("❌ Código incorrecto.")
            return False

# 🔍 Prueba de recuperación por correo
correo = RecuperacionCorreo("usuario@example.com")
correo.enviar_codigo()
codigo_usuario = input("Introduce el código recibido en tu correo: ")
correo.verificar_codigo(codigo_usuario)
```

---

## **📌 Explicación de la Implementación**

1. **Generamos un código aleatorio de 6 dígitos**.
2. **Usamos `smtplib` para enviar el código por correo**.
3. **Comparamos el código ingresado con el código enviado** antes de permitir el cambio de contraseña.

---

## **📝 Conclusión**

✅ **Ahora almacenamos los usuarios en una base de datos.**
✅ **Hemos agregado recuperación de contraseña con preguntas de seguridad.**
✅ **También hemos añadido recuperación por correo con un código.**

¿Quieres que integremos todo en un solo sistema con una interfaz más amigable? 🚀