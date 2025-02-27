# 2.2 Escaneo de múltiples puertos

# Si queremos escanear más de un puerto, podemos especificar un rango:


import nmap

scanner = nmap.PortScanner()

scanner.scan('192.168.1.1', '22,80,443,8080')

for port in scanner['192.168.1.1']['tcp']:
    print(f"[*] Puerto {port}: {scanner['192.168.1.1']['tcp'][port]['state']}")