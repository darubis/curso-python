_____


La **criptografía** es el estudio y la práctica de técnicas para asegurar la comunicación y la información, protegiéndola de accesos no autorizados. Se basa en conceptos matemáticos y algoritmos para cifrar y descifrar datos.

En el mundo moderno, la criptografía se usa en casi todos los aspectos digitales: desde proteger contraseñas hasta asegurar transacciones bancarias y comunicaciones en aplicaciones de mensajería.

---

## 📌 Módulos de Criptografía en Python

Python ofrece varias bibliotecas para trabajar con criptografía, pero las más populares son:

1. **`hashlib`** – Para funciones hash (SHA-256, MD5, etc.).
2. **`hmac`** – Para autenticación con claves secretas.
3. **`pycryptodome`** – Para cifrado y descifrado de datos.
4. **`cryptography`** – Para algoritmos de cifrado moderno y gestión de claves.

Veamos cómo usar cada una de ellas.

---

### 🔹 1. Funciones Hash con `hashlib`

El hashing convierte un mensaje en una cadena de longitud fija. Es útil para almacenar contraseñas de forma segura.

```python
import hashlib

# Hash SHA-256 de un mensaje
mensaje = "Hola, criptografía en Python"
hash_obj = hashlib.sha256(mensaje.encode())
print("Hash SHA-256:", hash_obj.hexdigest())
```

📌 **Aplicaciones reales**: Almacenamiento seguro de contraseñas, firmas digitales.

---

### 🔹 2. HMAC para Autenticación con `hmac`

HMAC (Hash-based Message Authentication Code) se usa para verificar la integridad de los datos con una clave secreta.

```python
import hmac
import hashlib

mensaje = b"Mensaje importante"
clave = b"secreta"

hmac_obj = hmac.new(clave, mensaje, hashlib.sha256)
print("HMAC:", hmac_obj.hexdigest())
```

📌 **Aplicaciones reales**: Autenticación en APIs y tokens de sesión.

---

### 🔹 3. Cifrado Simétrico con `pycryptodome`

En el cifrado simétrico, la misma clave se usa para cifrar y descifrar.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Generar clave y datos
clave = os.urandom(16)  # Clave de 16 bytes (AES-128)
mensaje = b"Texto secreto"
cipher = AES.new(clave, AES.MODE_CBC)
iv = cipher.iv  # Vector de inicialización
cifrado = cipher.encrypt(pad(mensaje, AES.block_size))

# Descifrado
cipher_dec = AES.new(clave, AES.MODE_CBC, iv)
descifrado = unpad(cipher_dec.decrypt(cifrado), AES.block_size)

print("Mensaje cifrado:", cifrado.hex())
print("Mensaje descifrado:", descifrado.decode())
```

📌 **Aplicaciones reales**: Cifrado de archivos y bases de datos.

---

### 🔹 4. Cifrado Asimétrico con `cryptography`

En criptografía asimétrica, se usa una clave pública para cifrar y una clave privada para descifrar.

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar clave RSA
clave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Exportar clave pública
clave_publica = clave_privada.public_key()
pub_key_pem = clave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Clave pública:", pub_key_pem.decode())
```

📌 **Aplicaciones reales**: HTTPS (SSL/TLS), autenticación con claves SSH.

---

## 🚀 Aplicaciones en el Mundo Real

1. **Contraseñas seguras**: Se almacenan usando hashing en bases de datos.
2. **Cifrado de archivos**: Protección de datos en discos duros y bases de datos.
3. **Firmas digitales**: Verificación de documentos y transacciones financieras.
4. **Seguridad en aplicaciones web**: Uso de HTTPS para encriptar datos en línea.
5. **Autenticación en sistemas**: Uso de tokens criptográficos y 2FA.

---

### 🎯 Conclusión

La criptografía en Python es poderosa y esencial para la seguridad de la información. Dependiendo del caso de uso, podemos elegir entre **hashing, cifrado simétrico o asimétrico**.

Si quieres profundizar más, dime qué aspecto te interesa más: ¿cifrado simétrico, asimétrico, hashing, o autenticación? 🔍