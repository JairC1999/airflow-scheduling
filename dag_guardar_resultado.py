# dag_guardar_resultado.py
from common_args import default_args
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime

# Función para guardar el resultado en MySQL
def guardar_resultado():
    mysql_hook = MySqlHook(mysql_conn_id="mysql_default")
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS horario_optimo")
    cursor.execute("""
        CREATE TABLE horario_optimo (
            aula VARCHAR(50),
            horario VARCHAR(50)
        );
    """)

    # Guardar resultado ficticio (mejor horario)
    mejor_horario = [("Aula 101", "08:00-10:00"), ("Aula 102", "10:00-12:00")]
    for aula, horario in mejor_horario:
        cursor.execute("INSERT INTO horario_optimo (aula, horario) VALUES (%s, %s)", (aula, horario))
    connection.commit()

# Configuración del DAG
with DAG(dag_id="dag_guardar_resultado", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    guardar_resultado_task = PythonOperator(
        task_id="guardar_resultado",
        python_callable=guardar_resultado
    )