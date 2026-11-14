import socket
import time

HOST = '0.0.0.0'  # Escucha en todas las interfaces de red disponibles
PUERTO = 5000

def iniciar_worker():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite reutilizar el puerto inmediatamente tras reiniciar el script
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PUERTO))
    servidor.listen(5)
    
    print(f"[*] Nodo Worker activo y escuchando en el puerto {PUERTO}...")

    while True:
        conn, addr = servidor.accept()
        try:
            datos = conn.recv(1024).decode('utf-8')
            if datos:
                print(f"[+] Procesando petición desde el coordinador ({addr[0]}): {datos}")
                
                # Simulación de carga de procesamiento distribuido
                time.sleep(1)
                
                # Enviar acuse de recibo de vuelta al coordinador
                conn.send(b'OK - Tarea completada con exito')
        finally:
            conn.close()

if __name__ == "__main__":
    iniciar_worker()
