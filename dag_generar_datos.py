from common_args import default_args
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from faker import Faker
import os
import csv

# Función para generar datos falsos
def generar_datos():
    fake = Faker()
    # Usar una ruta válida basada en las configuraciones de Docker
    ruta_csv = os.path.join("/opt/airflow/dags", "datos_iniciales.csv")
    with open(ruta_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["profesor", "asignatura", "aula", "horario"])
        horarios = ["08:00-10:00", "10:00-12:00", "14:00-16:00", "16:00-18:00"]
        aulas = ["Aula 101", "Aula 102", "Aula 103"]
        for _ in range(20):  # Generar 10 registros
            writer.writerow([fake.name(), fake.job(), fake.random_element(aulas), fake.random_element(horarios)])
    print(f"Archivo generado en: {ruta_csv}")

# Configuración del DAG
with DAG(
    dag_id="dag_generar_datos",
    default_args=default_args,  # Importar configuración compartida
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    generar_datos_task = PythonOperator(
        task_id="generar_datos",
        python_callable=generar_datos
    )
