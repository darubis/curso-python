Has hecho un buen trabajo implementando el método `cambiar_contrasena`, pero hay algunos errores y mejoras que podemos hacer:

---

### **Errores y Mejoras**
1. **Error en la verificación de contraseña en `cambiar_contrasena`**  
   - Estás aplicando `hashlib.sha256()` en `current_password` antes de pasarlo a `verificar_password()`, pero ese método ya lo has definido para hacer la comparación internamente.  
   - Solución: Pasa `current_password` directamente a `verificar_password()`.

2. **El contador de intentos no está funcionando correctamente**  
   - El bucle `while contador <= 3:` no restringe los intentos correctamente porque la variable `contador` se reinicia cada vez que se llama al método.  
   - Solución: Usa un atributo `intentos_fallidos` en la clase para hacer un seguimiento de los intentos de cambio de contraseña.

3. **Falta una condición para salir del bucle**  
   - Si la contraseña es incorrecta, el código seguirá corriendo y no evitará nuevos intentos después de 3 fallos.  
   - Solución: Agregar una condición para detener el cambio de contraseña después del número máximo de intentos.

4. **No hay mensaje de éxito tras cambiar la contraseña**  
   - Se debería mostrar un mensaje cuando la contraseña ha sido cambiada exitosamente.

---

### **Corrección del Código**
```python
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
            self.password_hash = self.hash_password(new_password)
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

```

---

### **Mejoras y Explicación**
✅ **Corrección en la verificación de contraseña**  
✅ **Límite de intentos de cambio de contraseña**  
✅ **Evita que un atacante intente cambiar la contraseña muchas veces (protección contra fuerza bruta)**  
✅ **Mensajes claros para el usuario**  

---

**Siguiente Paso:**  
Si quieres mejorar aún más, podríamos implementar **salteo en el hash de contraseñas** usando `bcrypt` en lugar de `hashlib`. ¿Te interesa aprenderlo?