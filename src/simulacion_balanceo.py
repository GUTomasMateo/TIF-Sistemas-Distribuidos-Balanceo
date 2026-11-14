import simpy
import random
# Parámetros de la simulación
TIEMPO_SIMULACION = 100  # Tiempo total de simulación
TASA_LLEGADA = 5         # Intervalo medio entre llegada de tareas (segundos)

class ClusterSimulacion:
    def __init__(self, env, num_nodos, politica):
        self.env = env
        self.num_nodos = num_nodos
        self.politica = politica
        # Cada nodo es un recurso con capacidad 1 (procesa una tarea a la vez)
        self.servidores = [simpy.Resource(env, capacity=1) for _ in range(num_nodos)]
        self.cargas = [0] * num_nodos
        self.indice_rr = 0
        self.tiempo_espera_total = 0
        self.tareas_completadas = 0

    def seleccionar_nodo(self):
        if self.politica == "RoundRobin":
            nodo = self.indice_rr
            self.indice_rr = (self.indice_rr + 1) % self.num_nodos
            return nodo
        elif self.politica == "MenosCargado":
            # Selecciona el nodo con menor cantidad de carga actual
            return self.cargas.index(min(self.cargas))
        elif self.politica == "PowerOfTwo":
            # El poder de dos opciones: elige 2 al azar y se queda con el menos cargado
            n1, n2 = random.sample(range(self.num_nodos), 2)
            return n1 if self.cargas[n1] <= self.cargas[n2] else n2

    def tarea(self, id_tarea):
        llegada = self.env.now
        nodo_idx = self.seleccionar_nodo()
        
        self.cargas[nodo_idx] += 1
        
        with self.servidores[nodo_idx].request() as req:
            yield req
            # Tiempo de procesamiento de la tarea
            proceso_tiempo = random.uniform(1.0, 3.0)
            yield self.env.timeout(proceso_tiempo)
            
        self.cargas[nodo_idx] -= 1
        espera = self.env.now - llegada
        self.tiempo_espera_total += espera
        self.tareas_completadas += 1

def generar_tareas(env, cluster):
    id_t = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / TASA_LLEGADA))
        env.process(cluster.tarea(id_t))
        id_t += 1

# Ejecución de pruebas para diferentes escalas de nodos
def ejecutar_experimentos():
    escalas = [16, 64, 256, 512]
    politicas = ["RoundRobin", "MenosCargado", "PowerOfTwo"]

    print(f"{'Nodos':<8} | {'Política':<15} | {'Tiempo Promedio de Espera':<25}")
    print("-" * 55)

    for nodos in escalas:
        for pol in politicas:
            random.seed(42)  # Para reproducibilidad de resultados
            env = simpy.Environment()
            cluster = ClusterSimulacion(env, nodos, pol)
            env.process(generar_tareas(env, cluster))
            env.run(until=TIEMPO_SIMULACION)

            promedio_espera = cluster.tiempo_espera_total / max(1, cluster.tareas_completadas)
            print(f"{nodos:<8} | {pol:<15} | {promedio_espera:.4f} segundos")

if __name__ == "__main__":
    print("[*] Iniciando simulaciones con SimPy para el informe técnico...")
    ejecutar_experimentos()
