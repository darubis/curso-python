import nmap

def escaneo_completo(target):
    scanner = nmap.PortScanner()
    print(f"Escaneando {target}...")
    
    scanner.scan(target, arguments="-sS -sV -O --script vuln")
    
    for host in scanner.all_hosts():
        print(f"\n[+] Host encontrado: {host} ({scanner[host].state()})")

        if 'osmatch' in scanner[host]:
            print(f"[*] Posible OS: {scanner[host]['osmatch'][0]['name']}")

        for port, info in scanner[host]['tcp'].items():
            print(f"[*] Puerto {port}: {info['state']} ({info['name']} - {info.get('version', 'Desconocida')})")

        if 'hostscript' in scanner[host]:
            print("\n[!] Scripts NSE detectaron posibles vulnerabilidades:")
            for result in scanner[host]['hostscript']:
                print(f" - {result['id']}: {result['output']}")

target = input("Ingrese la IP o rango de red: ")
escaneo_completo(target)