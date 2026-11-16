# Trabajo Integrador Final: Sistemas Operativos Distribuidos

Repositorio oficial para la implementación, simulación y evaluación experimental de estrategias de balanceo de carga (**Round Robin Estático**, **Menos Cargado Centralizado** y **El Poder de Dos Opciones**) en entornos distribuidos.

---

## Requisitos Previos y Entorno
* **Virtualización:** Oracle VirtualBox y Vagrant instalados.
* **Lenguaje:** Python 3.x con las librerías `simpy`, `pandas` y `matplotlib` instaladas.

---

## Guía de Reproducción Paso a Paso

### Paso 1: Despliegue de la Infraestructura con Vagrant
1. Clona este repositorio y abre una terminal en la carpeta raíz del proyecto.
2. Levanta los tres nodos virtuales (Coordinador y dos Workers) configurados automáticamente en la red privada *Host-Only*:
   ```bash
   vagrant up

### Paso 2: Descarga de archivos y ejecución
1. Primero carga los archivos en las maquinas virtuales, worker.py para los nodos y coordinador y simulacion en la pcs coordinadora.
2. Luego ejecuta los comandos en orden, primero el worker.py en ambos nodos y por ultimo el coordinador.py y luego el simulador. Se ejecuta el coordinador primero ya que busca los nodos disponibles, si es que no se ejecutaron los worker.py previamente, este lanzara un error ya que no estan disponibles los nodo.
