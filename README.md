<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Airflow Scheduling</title>
</head>
<body>
    <h1>Airflow Scheduling</h1>
    <p>
        Este repositorio contiene una configuración completa para implementar un entorno de <strong>Apache Airflow</strong> utilizando <strong>Docker Compose</strong>. Además, incluye varios DAGs diseñados para automatizar procesos relacionados con la <strong>optimización de horarios escolares</strong>.
    </p>

    <hr>

    <h2>Tabla de Contenidos</h2>
    <ol>
        <li><a href="#descripcion">Descripción</a></li>
        <li><a href="#requisitos-previos">Requisitos Previos</a></li>
        <li><a href="#configuracion-del-entorno">Configuración del Entorno</a></li>
        <li><a href="#estructura-del-proyecto">Estructura del Proyecto</a></li>
        <li><a href="#uso-de-los-dags">Uso de los DAGs</a></li>
        <li><a href="#contribuciones">Contribuciones</a></li>
        <li><a href="#licencia">Licencia</a></li>
    </ol>

    <hr>

    <h2 id="descripcion">Descripción</h2>
    <p>
        Este proyecto utiliza Apache Airflow para gestionar flujos de trabajo enfocados en la generación, evaluación y optimización de horarios escolares. Los componentes clave incluyen:
    </p>
    <ul>
        <li>Contenedores Docker para Airflow, MySQL, Redis y PostgreSQL.</li>
        <li>DAGs personalizables que implementan un <strong>algoritmo genético</strong> para la optimización de horarios.</li>
        <li>Funcionalidades para generar datos de prueba, cargar datos en la base de datos y almacenar los resultados en MySQL.</li>
    </ul>

    <hr>

    <h2 id="requisitos-previos">Requisitos Previos</h2>
    <p>Antes de empezar, asegúrate de tener instalados:</p>
    <ul>
        <li>Docker y Docker Compose.</li>
        <li>Python 3.8 o superior (opcional para modificaciones locales).</li>
    </ul>

    <hr>

    <h2 id="configuracion-del-entorno">Configuración del Entorno</h2>
    <ol>
        <li>Clona este repositorio:
            <pre>
git clone https://github.com/JairC1999/airflow-scheduling.git
cd airflow-scheduling
            </pre>
        </li>
        <li>Inicia los servicios:
            <pre>
docker-compose up -d
            </pre>
        </li>
        <li>Accede a la interfaz web de Airflow:
            <ul>
                <li><strong>URL:</strong> <a href="http://localhost:8080">http://localhost:8080</a></li>
                <li><strong>Usuario:</strong> admin</li>
                <li><strong>Contraseña:</strong> admin</li>
            </ul>
        </li>
    </ol>

    <hr>

    <h2 id="estructura-del-proyecto">Estructura del Proyecto</h2>
    <pre>
airflow-scheduling/
├── docker-compose.yaml          # Configuración de Docker Compose
├── dags/                        # Directorio de DAGs
│   ├── common_args.py           # Configuración compartida para DAGs
│   ├── dag_algoritmo_genetico.py # DAG para el algoritmo genético
│   ├── dag_cargar_datos.py       # DAG para cargar datos en MySQL
│   ├── dag_evaluacion_inicial.py # DAG para generar población inicial
│   ├── dag_generar_datos.py      # DAG para generar datos falsos
│   ├── dag_guardar_resultado.py  # DAG para guardar resultados en MySQL
├── datos_iniciales.csv          # Archivo de datos de prueba
├── plugins/                     # Directorio para plugins de Airflow (vacío)
├── logs/                        # Directorio para logs de Airflow (generado automáticamente)
├── README.md                    # Documentación del proyecto
    </pre>

    <hr>

    <h2 id="uso-de-los-dags">Uso de los DAGs</h2>
    <ol>
        <li><strong>Generar datos iniciales:</strong>
            <p>Ejecuta el DAG <code>dag_generar_datos</code> para crear un archivo CSV con datos de prueba.</p>
        </li>
        <li><strong>Cargar datos en MySQL:</strong>
            <p>Ejecuta el DAG <code>dag_cargar_datos</code> para cargar los datos del CSV en la base de datos.</p>
        </li>
        <li><strong>Ejecutar el algoritmo genético:</strong>
            <p>Ejecuta el DAG <code>dag_algoritmo_genetico</code> para optimizar los horarios escolares.</p>
        </li>
        <li><strong>Guardar el resultado:</strong>
            <p>Ejecuta el DAG <code>dag_guardar_resultado</code> para almacenar los horarios optimizados en MySQL.</p>
        </li>
    </ol>

    <hr>

    <h2 id="contribuciones">Contribuciones</h2>
    <p>Las contribuciones son bienvenidas. Si tienes mejoras, abre un <em>pull request</em> o crea un <em>issue</em> en este repositorio.</p>

    <hr>

    <h2 id="licencia">Licencia</h2>
    <p>Este proyecto está licenciado bajo la <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
