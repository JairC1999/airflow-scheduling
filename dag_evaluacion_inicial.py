# dag_evaluacion_inicial.py
from common_args import default_args
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import random

# Función para generar población inicial
def evaluacion_inicial():
    mysql_hook = MySqlHook(mysql_conn_id="mysql_default")
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT aula, horario FROM datos_iniciales")
    aulas_horarios = cursor.fetchall()

    poblacion = []
    for _ in range(10):  # Población de 10 individuos
        individuo = random.sample(aulas_horarios, len(aulas_horarios))
        poblacion.append(individuo)

    print(f"Población inicial generada: {poblacion}")

# Configuración del DAG
with DAG(dag_id="dag_evaluacion_inicial", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    evaluacion_inicial_task = PythonOperator(
        task_id="evaluacion_inicial",
        python_callable=evaluacion_inicial
    )