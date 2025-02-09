from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
import csv
import os

# Función para cargar datos en MySQL
def cargar_datos():
    try:
        mysql_hook = MySqlHook(mysql_conn_id='mysql_default')
        connection = mysql_hook.get_conn()
        cursor = connection.cursor()

        # Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_iniciales (
                profesor VARCHAR(100),
                asignatura VARCHAR(100),
                aula VARCHAR(50),
                horario VARCHAR(50)
            );
        """)

        # Ruta del archivo CSV
        ruta_csv = os.path.join("/opt/airflow/dags", "datos_iniciales.csv")

        # Verifica si el archivo existe antes de intentar leerlo
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"El archivo {ruta_csv} no existe. Genera primero el archivo CSV.")

        # Insertar datos desde el archivo CSV
        with open(ruta_csv, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                cursor.execute(
                    "INSERT INTO datos_iniciales (profesor, asignatura, aula, horario) VALUES (%s, %s, %s, %s)", 
                    row
                )

        # Confirmar cambios en la base de datos
        connection.commit()
        print("Datos cargados exitosamente en la base de datos.")

    except Exception as e:
        print(f"Error al cargar datos: {e}")
        raise

# Configuración del DAG
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dag_cargar_datos",
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    description="Carga los datos iniciales desde un archivo CSV a la base de datos MySQL."
) as dag:
    cargar_datos_task = PythonOperator(
        task_id="cargar_datos",
        python_callable=cargar_datos
    )
