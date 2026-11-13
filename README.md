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
