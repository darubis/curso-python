# 2.3 Detectando servicios en los puertos abiertos

# Para identificar los servicios que corren en los puertos abiertos, usamos la opción -sV de nmap:

import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168.1.1', '1-1000', '-sV')

for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(f"Estado: {scanner[host].state()}")

    for port, data in scanner[host]['tcp'].items():
        print(f"Puerto: {port}, Estado: {data['state']}, Servicio: {data['name']}, Versión: {data.get('version', 'Desconocida')}")
