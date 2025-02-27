import nmap

scanner = nmap.PortScanner()
scanner.scan(hosts='192.168.1.0/24', arguments='-sn')

print("Hosts activos en la red:")
for host in scanner.all_hosts():
    print(f"[*] {host} - {scanner[host].state()}")