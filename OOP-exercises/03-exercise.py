# Ejercicio 3: Simulación de Ataque de Fuerza Bruta

# Descripción:
# Crea una clase BruteForceSimulator que simule un ataque de fuerza bruta sobre una contraseña dada.
# Características:

#     La clase debe recibir una contraseña y un diccionario de palabras (puede ser una lista predefinida).
#     Implementa un método simulate() que pruebe cada palabra del diccionario hasta encontrar la contraseña correcta.
#     Debe contar el número de intentos realizados.
#     Al finalizar, muestra cuánto tiempo tomó realizar el ataque (usa time).

# Restricciones:

#     Implementa buenas prácticas como encapsulamiento y separación de responsabilidades.

import time
import hashlib

# Diccionario de contraseñas en texto plano
passwords_dict = [
    "123456", "password", "123456789", "qwerty", "micontrasena123",
    "1234567", "abc123", "password1", "contrasena23"
]

class BruteForceSimulator:
    def __init__(self, password_hash, passwords_list):
        self.password_hash = password_hash
        self.passwords_list = passwords_list
        self.attempts = 0

    def hash_password(self, password):
        """Genera el hash SHA-256 de una contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()

    def simulate(self):
        """Simula un ataque de fuerza bruta probando contraseñas de un diccionario"""
        start_time = time.time()

        for password in self.passwords_list:
            self.attempts += 1
            hashed_attempt = self.hash_password(password)

            print(f"Intento {self.attempts}: Probando '{password}'...")  # Simulación visual
            time.sleep(0.5)  # Simula el tiempo de cada intento

            if hashed_attempt == self.password_hash:
                end_time = time.time()
                print(f"\n[✔] Contraseña encontrada: '{password}'")
                print(f"Tiempo transcurrido: {end_time - start_time:.2f} segundos")
                print(f"Intentos realizados: {self.attempts}")
                return

        end_time = time.time()
        print("\n[✘] Contraseña no encontrada en el diccionario.")
        print(f"Tiempo transcurrido: {end_time - start_time:.2f} segundos")
        print(f"Intentos realizados: {self.attempts}")

# Definir la contraseña objetivo
password_to_crack = "contrasena23"
password_hash_to_crack = hashlib.sha256(password_to_crack.encode()).hexdigest()

# Instancia del simulador
brute_force = BruteForceSimulator(password_hash_to_crack, passwords_dict)
brute_force.simulate()