import socket
import json

# IPs estáticas de los workers en la red Host-Only (enp0s8)
WORKERS = [
    {"id": 0, "ip": "192.168.56.11", "port": 5000, "carga": 0},
    {"id": 1, "ip": "192.168.56.12", "port": 5000, "carga": 0}
]

def enviar_tarea(worker_ip, worker_port, tarea):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((worker_ip, worker_port))
        s.sendall(json.dumps(tarea).encode('utf-8'))
        respuesta = s.recv(1024).decode('utf-8')
        return json.loads(respuesta)

def balanceador_round_robin(tareas):
    for idx, tarea in enumerate(tareas):
        w = WORKERS[idx % len(WORKERS)]
        print(f"[*] Asignando Tarea {tarea['id']} a Worker {w['id']} ({w['ip']}) via Round Robin")
        enviar_tarea(w['ip'], w['port'], tarea)

if __name__ == "__main__":
    lotes_prueba = [{"id": i, "costo": 2} for i in range(6)]
    print("[*] Iniciando distribución de tareas desde el Coordinador...")
    balanceador_round_robin(lotes_prueba)