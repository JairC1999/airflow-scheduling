# dag_algoritmo_genetico.py
from common_args import default_args
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import random

# Función para ejecutar el algoritmo genético
def algoritmo_genetico():
    mysql_hook = MySqlHook(mysql_conn_id="mysql_default")
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT aula, horario FROM datos_iniciales")
    aulas_horarios = cursor.fetchall()

    poblacion = [random.sample(aulas_horarios, len(aulas_horarios)) for _ in range(10)]

    for generacion in range(5):  # 5 generaciones
        fitness_scores = []
        for individuo in poblacion:
            score = len(set(individuo))  # Penalizar repeticiones
            fitness_scores.append((score, individuo))

        fitness_scores.sort(reverse=True, key=lambda x: x[0])
        poblacion = [x[1] for x in fitness_scores[:5]]  # Selección

        # Cruza y mutación
        nuevos_individuos = []
        for _ in range(5):
            p1, p2 = random.sample(poblacion, 2)
            hijo = p1[:len(p1)//2] + p2[len(p2)//2:]  # Cruza simple
            if random.random() < 0.1:  # Mutación
                idx = random.randint(0, len(hijo) - 1)
                hijo[idx] = random.choice(aulas_horarios)
            nuevos_individuos.append(hijo)

        poblacion.extend(nuevos_individuos)

    mejor_individuo = max(poblacion, key=lambda x: len(set(x)))
    print(f"Mejor horario: {mejor_individuo}")

# Configuración del DAG
with DAG(dag_id="dag_algoritmo_genetico", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    algoritmo_genetico_task = PythonOperator(
        task_id="ejecutar_algoritmo_genetico",
        python_callable=algoritmo_genetico
    )