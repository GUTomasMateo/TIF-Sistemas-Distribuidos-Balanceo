import socket
import time

# Direcciones IP de los nodos workers en la red del clúster
WORKERS = ['192.168.1.95', '192.168.1.96']
PUERTO = 5000

def ejecutar_coordinador():
    print("[*] Iniciando Coordinador de Tareas Distribuidas...")
    contador = 0
    
    try:
        while True:
            for ip in WORKERS:
                contador += 1
                print(f"[*] Enviando Tarea #{contador} al Worker ({ip}:{PUERTO})...")
                
                # Establecer comunicación TCP mediante Sockets
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((ip, PUERTO))
                    s.send(f'tarea_{contador}'.encode('utf-8'))
                    
                    # Esperar y recibir la confirmación del worker
                    respuesta = s.recv(1024).decode('utf-8')
                    print(f"[+] Respuesta recibida de {ip}: {respuesta}")
                
                time.sleep(1) # Intervalo de control entre solicitudes
    except KeyboardInterrupt:
        print("\n[*] Coordinador detenido manualmente por el usuario.")

if __name__ == "__main__":
    ejecutar_coordinador()
