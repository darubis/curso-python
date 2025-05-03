____

Tanto `hashlib` como `bcrypt` se usan para el **hashing** (cifrado unidireccional) de datos, especialmente contraseñas. Sin embargo, tienen diferencias clave en **seguridad, propósito y funcionamiento**.

---

## 🔹 **1. `hashlib` (SHA-256, MD5, etc.)**

📌 **¿Qué es?**  
`hashlib` es un módulo estándar de Python que implementa funciones de hash como **SHA-256, SHA-512, MD5** y otras. Se usa para generar un **hash rápido y eficiente**, pero **sin protección contra ataques de fuerza bruta**.

📌 **Cómo funciona:**

1. Convierte un dato (como una contraseña) en una cadena de longitud fija.
2. El mismo dato siempre generará el mismo hash.
3. No tiene "salt" incorporado (se puede agregar manualmente).
4. Es rápido, pero vulnerable a ataques de diccionario y fuerza bruta.

🔹 **Ejemplo con SHA-256:**

```python
import hashlib

contraseña = "MiContraseñaSegura"
hash_sha256 = hashlib.sha256(contraseña.encode()).hexdigest()

print("SHA-256 Hash:", hash_sha256)
```

🔹 **Ejemplo con "salt" manual para mejorar seguridad:**

```python
import hashlib
import os

contraseña = "MiContraseñaSegura"
salt = os.urandom(16)  # Genera un salt aleatorio
hash_con_salt = hashlib.pbkdf2_hmac('sha256', contraseña.encode(), salt, 100000)

print("Hash con salt:", hash_con_salt.hex())
print("Salt:", salt.hex())
```

📌 **Desventaja:**

- Rápido, pero **demasiado predecible**.
- No tiene una protección integrada contra ataques de fuerza bruta.

📌 **¿Para qué se usa?**  
✔️ Hashing de archivos (para verificar integridad).  
✔️ Generar checksums.  
✔️ Firmas digitales.

---

## 🔹 **2. `bcrypt` (Optimizado para contraseñas)**

📌 **¿Qué es?**  
`bcrypt` es una biblioteca especializada en el **hashing seguro de contraseñas**. Usa el algoritmo Blowfish y tiene características que lo hacen **mucho más seguro que `hashlib` para contraseñas**.

📌 **Cómo funciona:**

1. Usa un mecanismo de "work factor" (coste computacional) para **hacer que los hashes sean más lentos**, lo que protege contra ataques de fuerza bruta.
2. **Siempre genera un hash diferente**, porque usa un **salt** aleatorio incorporado.
3. Permite **verificar contraseñas fácilmente** comparando el hash almacenado con una nueva entrada.

🔹 **Ejemplo con `bcrypt`:**

```python
import bcrypt

# Generar un hash seguro con salt automático
contraseña = b"MiContraseñaSegura"
hash_bcrypt = bcrypt.hashpw(contraseña, bcrypt.gensalt())

print("Hash bcrypt:", hash_bcrypt)
```

🔹 **Verificar una contraseña:**

```python
contraseña_ingresada = b"MiContraseñaSegura"

if bcrypt.checkpw(contraseña_ingresada, hash_bcrypt):
    print("✅ Contraseña correcta")
else:
    print("❌ Contraseña incorrecta")
```

📌 **Ventajas:**  
✔️ **Más seguro que `hashlib` para contraseñas**.  
✔️ **Resistente a ataques de fuerza bruta** gracias a su coste computacional.  
✔️ **Salt incorporado** automáticamente.

📌 **¿Para qué se usa?**  
✔️ Almacenamiento seguro de contraseñas en bases de datos.  
✔️ Autenticación segura en sistemas web y aplicaciones.

---

## 🔥 **Resumen: ¿Cuál usar y cuándo?**

|Característica|`hashlib` (SHA-256, PBKDF2)|`bcrypt`|
|---|---|---|
|**Velocidad**|⚡ Muy rápido|🐢 Lento (pero seguro)|
|**Uso de salt automático**|❌ No (se debe agregar manualmente)|✅ Sí|
|**Resistencia a ataques de fuerza bruta**|❌ Débil|✅ Fuerte|
|**¿Genera el mismo hash siempre?**|✅ Sí (sin salt)|❌ No (usa salt aleatorio)|
|**Uso recomendado**|Integridad de datos, checksums, hashing rápido|Almacenamiento seguro de contraseñas|

📌 **Conclusión:**  
🔹 **Usa `bcrypt` para almacenar contraseñas** de forma segura en bases de datos.  
🔹 **Usa `hashlib` para hashing rápido**, como verificación de integridad de archivos o autenticación con HMAC.
