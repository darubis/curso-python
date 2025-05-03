### 🔒 **Hashing Seguro de Contraseñas con `bcrypt` en Python**  

Hasta ahora, hemos usado **SHA-256** para almacenar contraseñas, pero tiene una **debilidad importante**:  
✅ Es rápido, lo que lo hace vulnerable a ataques de **fuerza bruta** y **diccionario** con hardware especializado (como GPU o ASICs).  

💡 **Solución:** Usar `bcrypt`, que es un algoritmo de hashing más seguro porque:  
1. **Es lento de propósito**: Hace que los ataques de fuerza bruta sean mucho más difíciles.  
2. **Usa "salts" automáticamente**: Un salt es un dato aleatorio añadido antes de cifrar la contraseña, evitando ataques de diccionario y tablas rainbow.  

---

## **🔧 Instalación de `bcrypt`**
Si aún no lo tienes instalado, usa el siguiente comando en tu terminal o en el entorno de Python:
```sh
pip install bcrypt
```

---

## **🚀 Ejemplo 1: Cómo Funciona `bcrypt` en Python**
```python
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
```

### **📌 Explicación del Código**
1. `bcrypt.gensalt()` → Genera un **salt aleatorio** para cada usuario.  
2. `bcrypt.hashpw(password, salt)` → Aplica hashing con bcrypt y el salt.  
3. `bcrypt.checkpw(password_ingresada, hashed_password)` → Verifica la contraseña de manera segura.  

---

## **🔐 ¿Cómo se usa esto en el mundo real?**
🚀 **Casos de uso en ciberseguridad:**
- Sistemas de inicio de sesión seguros.  
- Almacenamiento seguro de contraseñas en bases de datos.  
- Protección contra ataques de fuerza bruta.  

**🔴 Ejemplo real:** Si una base de datos de contraseñas se filtra, las contraseñas con SHA-256 pueden ser descifradas fácilmente usando tablas precomputadas (**rainbow tables**). Con bcrypt, cada contraseña tiene un hash y salt únicos, lo que hace imposible usar estas tablas.  

---

## **🛠 Ejemplo 2: Integrando `bcrypt` en Nuestra Clase `Usuario`**
Ahora, reescribamos la clase `Usuario` para usar `bcrypt` en lugar de `hashlib`.  

```python
import bcrypt

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        """Cifra la contraseña usando bcrypt con un salt aleatorio"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def verificar_password(self, password):
        """Verifica si la contraseña ingresada coincide con el hash almacenado"""
        return bcrypt.checkpw(password.encode(), self.password_hash)

    def cambiar_contrasena(self, current_password, new_password):
        """Permite cambiar la contraseña de forma segura"""
        if self.verificar_password(current_password):
            self.password_hash = self.hash_password(new_password)
            print("✅ Contraseña cambiada exitosamente.")
        else:
            print("❌ Contraseña incorrecta. No se pudo cambiar.")

# 🔍 Prueba del sistema
usuario1 = Usuario("Alice", "segura123")
print("Hash almacenado:", usuario1.password_hash)

# Intento de acceso
password_ingresada = "segura123"
if usuario1.verificar_password(password_ingresada):
    print("✅ Acceso concedido")
else:
    print("❌ Acceso denegado")

# Intento de cambio de contraseña
usuario1.cambiar_contrasena("segura123", "nuevaSegura123")
```

---

## **✅ Beneficios de Usar `bcrypt`**
✅ **Evita ataques de diccionario y fuerza bruta** gracias a su lentitud controlada.  
✅ **Cada usuario tiene un hash único**, incluso si usan la misma contraseña.  
✅ **Se usa en la industria** para proteger contraseñas en bases de datos seguras.  

---

## **🔥 Reto para Ti**
Mejora la clase `Usuario` agregando:
1. **Límite de intentos de acceso fallidos** antes de bloquear al usuario.  
2. **Un sistema para desbloquear** al usuario después de un tiempo determinado.  

🔹 **Pista:** Usa un contador de intentos y una marca de tiempo para el desbloqueo.  
🔹 **Si necesitas ayuda, dime y lo resolvemos juntos. 🚀**