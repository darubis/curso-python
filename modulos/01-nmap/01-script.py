# 🚀 2. Uso básico del módulo nmap en Python
# 2.1 Escaneo de un solo puerto en un host

# Primero, importamos la librería y hacemos un escaneo básico.


import nmap

scanner = nmap.PortScanner()  
scanner.scan('192.168.1.1', '22')

print(scanner.all_hosts())  # Muestra los hosts escaneados
print(scanner['192.168.1.1'].state())  # Estado del host (up/down)
print(scanner['192.168.1.1']['tcp'][22]['state'])  # Estado del puerto 80 (open/closed)