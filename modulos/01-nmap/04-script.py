import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168.1.1', arguments='-O')

if 'osmatch' in scanner['192.168.1.1']:
    for os in scanner['192.168.1.1']['osmatch']:
        print(f"Probable OS: {os['name']} (Precisión: {os['accuracy']}%)")