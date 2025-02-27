import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168.1.1', arguments='--script smb-vuln*')

for host in scanner.all_hosts():
    print(f"Resultados de escaneo en {host}:")
    print(scanner[host].get('hostscript', 'Sin resultados'))
