____


El **salt** es un valor aleatorio que se añade a una contraseña antes de aplicar una función de hash. Su objetivo principal es **hacer que cada hash sea único**, incluso si dos usuarios tienen la misma contraseña.

🔹 **¿Por qué es importante?**

1. **Evita ataques de diccionario y tablas Rainbow**: Sin salt, los atacantes pueden usar bases de datos precalculadas de hashes (tablas Rainbow) para descifrar contraseñas rápidamente.
2. **Hace que los hashes sean únicos**: Incluso si dos personas tienen la misma contraseña, los hashes serán diferentes debido al salt.

---

### 🔹 **Ejemplo sin Salt (Inseguro)**

Si dos usuarios tienen la misma contraseña y usamos `hashlib`, generarán el mismo hash:

```python
import hashlib

contraseña1 = "password123"
contraseña2 = "password123"

hash1 = hashlib.sha256(contraseña1.encode()).hexdigest()
hash2 = hashlib.sha256(contraseña2.encode()).hexdigest()

print(hash1)  # Ambos hashes serán iguales ❌
print(hash2)
```

📌 **Problema**: Un atacante que tenga acceso a los hashes puede compararlos con una tabla precalculada y descifrar la contraseña rápidamente.

---

### 🔹 **Ejemplo con Salt (Seguro)**

Para evitar este problema, agregamos un **salt aleatorio** antes de hacer el hash:

```python
import hashlib
import os

contraseña = "password123"
salt = os.urandom(16)  # Genera un salt aleatorio de 16 bytes
hash_con_salt = hashlib.pbkdf2_hmac('sha256', contraseña.encode(), salt, 100000)

print("Salt:", salt.hex())
print("Hash con Salt:", hash_con_salt.hex())
```

📌 **Ventaja**:  
✔️ Cada vez que ejecutamos el código, obtenemos un hash diferente porque el salt cambia en cada intento.  
✔️ Hace imposible que un atacante use una tabla precalculada de hashes para descifrar la contraseña.

---

### 🔹 **Salt en `bcrypt`**

El módulo `bcrypt` ya **incorpora automáticamente un salt**, por lo que no es necesario generarlo manualmente:

```python
import bcrypt

contraseña = b"password123"
hash_bcrypt = bcrypt.hashpw(contraseña, bcrypt.gensalt())

print("Hash con bcrypt:", hash_bcrypt)
```

Cada vez que ejecutemos esto, el hash será diferente porque `gensalt()` genera un salt único cada vez.

---

## 🚀 **Resumen**

|**Característica**|**Sin Salt**|**Con Salt**|
|---|---|---|
|¿Siempre genera el mismo hash?|✅ Sí|❌ No|
|¿Protege contra tablas Rainbow?|❌ No|✅ Sí|
|¿Es más seguro?|❌ No|✅ Sí|
|¿Usado en `bcrypt`?|❌ No|✅ Sí (automático)|

📌 **Conclusión**: **Siempre usa Salt** cuando trabajes con contraseñas. Si usas `bcrypt`, ya lo añade automáticamente. 🚀