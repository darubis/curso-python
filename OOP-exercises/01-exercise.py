# Ejercicio 1: Escáner de Puertos Simulado

# Descripción:
# Crea una clase llamada PortScanner que simule un escaneo de puertos en una dirección IP.

#     Debe tener atributos como ip_address y ports (una lista de números de puertos).
#     Incluye un método scan_ports() que recorra la lista de puertos y muestre si un puerto está abierto o cerrado. Puedes simular aleatoriamente el estado del puerto usando random.
#     Agrega un método report() que guarde los resultados del escaneo en un archivo.

# Restricciones:

#     Usa propiedades privadas para los atributos.
#     Asegúrate de aplicar encapsulamiento y métodos de acceso si es necesario.

import nmap

class PortScanner:
    def __init__(self, ip_address):
        self.__ip_address = ip_address
        self.__ports = []
        self.__scan_results = {}

    def add_ports(self, ports):
        """Agregar una lista de puertos a escanear."""
        if isinstance(ports, list) and all(isinstance(port, int) for port in ports):
            self.__ports.extend(ports)
        else:
            raise ValueError("Los puertos deben ser una lista de números enteros.")

    def scan_ports(self):
        """Realizar el escaneo de los puertos."""
        if not self.__ports:
            raise ValueError("No se han agregado puertos para escanear.")
        
        scanner = nmap.PortScanner()
        print(f"Escaneando {self.__ip_address} en los puertos: {self.__ports}")

        try:
            scan_result = scanner.scan(
                hosts=self.__ip_address,
                ports=",".join(map(str, self.__ports)),
                arguments='-sS'  # Escaneo SYN (requiere privilegios root)
            )
            self.__scan_results = scan_result
        except nmap.PortScannerError as e:
            print(f"Error en el escaneo: {e}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

    def report(self, output_file):
        """Generar un reporte del escaneo."""
        if not self.__scan_results:
            print("No hay resultados de escaneo para generar un reporte.")
            return

        with open(output_file, 'w') as file:
            file.write(f"Reporte de escaneo para {self.__ip_address}\n")
            file.write("=" * 40 + "\n")
            for port, info in self.__scan_results.get('scan', {}).get(self.__ip_address, {}).get('tcp', {}).items():
                state = info.get('state', 'unknown')
                service = info.get('name', 'unknown')
                file.write(f"Puerto {port}: {state} (Servicio: {service})\n")

        print(f"Reporte generado en {output_file}")

# Ejemplo de uso
if __name__ == "__main__":
    # Dirección IP a escanear
    target_ip = "192.168.1.1"  # Cambiar a la dirección IP de tu red
    ports_to_scan = [22, 80, 443]

    scanner = PortScanner(target_ip)
    scanner.add_ports(ports_to_scan)
    scanner.scan_ports()
    scanner.report("scan_report.txt")