# Airflow Scheduling

Este repositorio contiene una configuración completa para implementar un entorno de **Apache Airflow** utilizando **Docker Compose**. Además, incluye varios DAGs diseñados para automatizar procesos relacionados con la **optimización de horarios escolares**.

---

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Requisitos Previos](#requisitos-previos)
3. [Configuración del Entorno](#configuración-del-entorno)
4. [Uso de los DAGs](#uso-de-los-dags)

---

## Descripción

Este proyecto utiliza Apache Airflow para gestionar flujos de trabajo enfocados en la generación, evaluación y optimización de horarios escolares. Los componentes clave incluyen:

- Contenedores Docker para Airflow, MySQL, Redis y PostgreSQL.
- DAGs personalizables que implementan un **algoritmo genético** para la optimización de horarios.
- Funcionalidades para generar datos de prueba, cargar datos en la base de datos y almacenar los resultados en MySQL.

---

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados:

- Docker y Docker Compose.
- Python 3.8 o superior (opcional para modificaciones locales).

---

## Configuración del Entorno

1. Clona este repositorio:

   ```bash
   git clone https://github.com/JairC1999/airflow-scheduling.git
   cd airflow-scheduling

## Uso de los DAGs

Aquí está el flujo de trabajo recomendado para usar los DAGs incluidos en este proyecto:

1. **Generar datos iniciales**:
   - Ejecuta el DAG `dag_generar_datos` para crear un archivo CSV con datos de prueba.
   - Este archivo se guardará en la ruta especificada dentro del DAG.

2. **Cargar datos en MySQL**:
   - Ejecuta el DAG `dag_cargar_datos` para cargar los datos generados en la base de datos MySQL.
   - Asegúrate de que los servicios estén ejecutándose correctamente con Docker.

3. **Ejecutar el algoritmo genético**:
   - Ejecuta el DAG `dag_algoritmo_genetico` para optimizar los horarios escolares utilizando un algoritmo genético.

4. **Guardar el resultado**:
   - Ejecuta el DAG `dag_guardar_resultado` para almacenar los resultados del horario óptimo en una tabla de MySQL.

---

## .gitignore recomendado

Para mantener tu repositorio limpio y evitar subir archivos irrelevantes, utiliza el siguiente archivo `.gitignore`:

