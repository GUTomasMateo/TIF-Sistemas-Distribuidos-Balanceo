import socket
import time
import json

HOST = '0.0.0.0'  # Escucha en todas las interfaces de la red privada
PORT = 5000

def ejecutar_tarea(costo):
    # Simula el procesamiento de datos agrometeorológicos
    time.sleep(costo)
    return True

def iniciar_worker():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(5)
    print(f"[*] Worker escuchando en el puerto {PORT}...")

    while True:
        conn, addr = servidor.accept()
        datos = conn.recv(1024).decode('utf-8')
        if not datos:
            break
        
        mensaje = json.loads(datos)
        tarea_id = mensaje['id']
        costo = mensaje['costo']
        
        print(f"[+] Ejecutando tarea {tarea_id} (Costo: {costo}s)...")
        ejecutar_tarea(costo)
        
        respuesta = json.dumps({"estado": "OK", "tarea_id": tarea_id})
        conn.sendall(respuesta.encode('utf-8'))
        conn.close()

if __name__ == "__main__":
    iniciar_worker()