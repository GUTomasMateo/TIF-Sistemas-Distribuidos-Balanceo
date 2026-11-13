import simpy
import random
import pandas as pd

class SimuladorBalanceo:
    def __init__(self, env, num_workers, estrategia):
        self.env = env
        self.num_workers = num_workers
        self.estrategia = estrategia
        # Estado de carga de cada worker (cantidad de tareas activas/pendientes)
        self.cargas_workers = {i: 0 for i in range(num_workers)}
        self.cola_tareas = simpy.Store(env)
        self.metricas = []

    def seleccionar_nodo(self):
        if self.estrategia == "round_robin":
            # Round Robin Estático
            if not hasattr(self, 'rr_index'):
                self.rr_index = 0
            nodo = self.rr_index
            self.rr_index = (self.rr_index + 1) % self.num_workers
            return nodo

        elif self.estrategia == "menos_cargado":
            # Menos cargado (Centralizado): busca el worker con menor carga actual
            nodo = min(self.cargas_workers, key=self.cargas_workers.get)
            return nodo

        elif self.estrategia == "poder_dos_opciones":
            # Power of Two Choices: elige 2 nodos al azar y se queda con el menos cargado
            candidatos = random.sample(range(self.num_workers), 2)
            nodo = min(candidatos, key=lambda n: self.cargas_workers[n])
            return nodo

    def procesar_tarea(self, worker_id, tarea_id, costo_cpu):
        self.cargas_workers[worker_id] += costo_cpu
        inicio = self.env.now
        yield self.env.timeout(costo_cpu)
        fin = self.env.now
        self.cargas_workers[worker_id] -= costo_cpu
        
        self.metricas.append({
            'worker': worker_id,
            'tarea': tarea_id,
            'costo': costo_cpu,
            'inicio': inicio,
            'fin': fin,
            'tiempo_estancia': fin - inicio
        })

    def despachador(self, tareas):
        for idx, tarea in enumerate(tareas):
            worker_asignado = self.seleccionar_nodo()
            self.env.process(self.procesar_tarea(worker_asignado, tarea['id'], tarea['costo']))
            # Pequeño intervalo de despacho del coordinador
            yield self.env.timeout(0.01)

def ejecutar_simulacion(num_nodos, estrategia_nombre, num_tareas=500):
    env = simpy.Environment()
    # Generación de lotes de tareas con costos de CPU aleatorios
    lotes = [{'id': i, 'costo': random.randint(1, 10)} for i in range(num_tareas)]
    
    sim = SimuladorBalanceo(env, num_nodos, estrategia_nombre)
    env.process(sim.despachador(lotes))
    
    inicio_total = env.now
    env.run()
    makespan_total = env.now - inicio_total
    
    return makespan_total, sim.metricas

if __name__ == "__main__":
    print("[*] Iniciando pruebas de escalabilidad con SimPy...")
    escalas = [16, 64, 256, 512]
    estrategias = ["round_robin", "menos_cargado", "poder_dos_opciones"]
    
    resultados = []
    for nodos in escalas:
        for est in estrategias:
            makespan, _ = ejecutar_simulacion(nodos, est)
            print(f"Escala: {nodos:3d} nodos | Estrategia: {est:18s} | Makespan Total: {makespan:.2f}s")