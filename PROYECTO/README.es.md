"""
# Proyecto de Clasificación de Score Crediticio

Este proyecto tiene como objetivo desarrollar un modelo de clasificación para predecir el puntaje de crédito de los clientes basado en sus características financieras y de comportamiento.

## Estructura del Proyecto

El proyecto está organizado en varios directorios y archivos, que se detallan a continuación:

### Estructura del Directorio

PROYECTO-CLASIFICACION-DE-SCORE-CREDITICIO-MAIN/
├── __pycache__/  # Archivos de caché generados por Python
├── .conda/       # Configuraciones relacionadas con Conda (si aplica)
├── .vscode/      # Configuraciones de VS Code
│   └── settings.json  # Configuración específica del proyecto en VS Code
├── PROYECTO/     # Carpeta principal del proyecto
│   ├── data/     # Datos crudos y procesados
│   │   ├── Processed/
│   │   │   ├── Data_Red_modelar.csv
│   │   │   ├── Datos_modelar.csv
│   │   │   └── Df_mod_blanceado.csv
│   │   ├── raw/
│   │   │   ├── test.csv
│   │   │   └── train.csv
│   ├── models/   # Modelos entrenados y scripts relacionados
│   │   ├── Ejemplo.py  # Ejemplo de uso de un modelo
│   │   └── Prediccion_score_c_rf.pkl  # Modelo entrenado de Random Forest
│   ├── src/      # Código fuente del proyecto
│   │   ├── __pycache__/  # Archivos de caché generados por Python
│   │   ├── data/  # Scripts relacionados con la carga y manejo de datos
│   │   │   ├── database_credito.db  # Base de datos SQLite usada en el proyecto
│   │   │   ├── db_creacion.py  # Script para crear la base de datos
│   │   │   └── load_data_api.py  # Script para cargar datos desde una API
│   │   ├── Exploracion_datos/  # Notebooks de exploración y análisis de datos
│   │   │   ├── __pycache__/  # Archivos de caché generados por Python
│   │   │   ├── explore.ipynb  # Notebook para explorar los datos
│   │   │   ├── Feature_engineering.ipynb  # Notebook para ingeniería de características
│   │   │   └── mis_funciones.py  # Funciones auxiliares para la exploración de datos
│   │   ├── models_training/  # Notebooks relacionados con el entrenamiento de modelos
│   │   │   ├── optimizacion_random_forest.ipynb  # Notebook para optimización de Random Forest
│   │   │   └── Seleccion_modelo_clasificacion.ipynb  # Notebook para selección de modelos
│   │   ├── utils.py  # Utilidades y funciones auxiliares
│   │   ├── __init__.py  # Archivo para inicializar el módulo de Python
│   │   ├── .env  # Variables de entorno (no se debe compartir públicamente)
│   │   ├── .gitignore  # Archivos y carpetas que Git debe ignorar
│   │   ├── mis_funciones.py  # Funciones adicionales utilizadas en los notebooks
│   ├── README.es.md  # Archivo README en español
│   └── README.md  # Archivo README en inglés
├── requirements.txt  # Archivo de requisitos con las dependencias del proyecto
├── .gitattributes  # Configuración para Git LFS y otros atributos de Git
├── app.py  # Aplicación de despliegue usando Streamlit
└── outlier.ipynb  # Notebook para análisis de valores atípicos

### Descripción de Carpetas y Archivos

- `__pycache__/`: Contiene archivos de caché generados automáticamente por Python para acelerar la ejecución.
- `.conda/`: Puede contener configuraciones específicas relacionadas con entornos Conda.
- `.vscode/settings.json`: Configuración personalizada para Visual Studio Code que afecta el entorno de desarrollo.
- `PROYECTO/data/`: Carpeta que almacena tanto los datos crudos (`raw`) como los datos procesados (`processed`).
- `PROYECTO/models/`: Almacena los modelos entrenados y scripts de ejemplo para su utilización.
    - `Prediccion_score_c_rf.pkl`: Modelo de Random Forest entrenado y guardado.
    - `Ejemplo.py`: Script de ejemplo para cargar y utilizar el modelo guardado.
- `PROYECTO/src/`: Contiene todo el código fuente y los scripts necesarios para el manejo de datos, entrenamiento de modelos y análisis.
    - `data/`: Scripts relacionados con la creación, carga y manejo de bases de datos.
    - `Exploracion_datos/`: Notebooks para exploración, análisis de datos y generación de características.
    - `models_training/`: Notebooks dedicados al entrenamiento, optimización y evaluación de modelos de clasificación.
    - `utils.py`: Contiene funciones utilitarias que son usadas a lo largo del proyecto.
    - `.env`: Archivo donde se guardan las variables de entorno, como claves de API o configuraciones sensibles (excluido en `.gitignore`).
    - `.gitignore`: Lista de archivos y carpetas que no deben ser subidos al repositorio Git.
- `README.es.md`: Versión en español del archivo README.
- `README.md`: Archivo README principal, que típicamente está en inglés.
- `requirements.txt`: Archivo de requisitos con las dependencias del proyecto.
- `.gitattributes`: Configuración para Git LFS y otros atributos de Git.
- `app.py`: Aplicación de despliegue usando Streamlit.
- `outlier.ipynb`: Notebook para análisis de valores atípicos.

## Instrucciones de Uso

1. Clonar el repositorio: `git clone <URL-del-repositorio>`
2. Configurar el entorno: Se recomienda crear un entorno virtual e instalar las dependencias utilizando el archivo `requirements.txt`.
3. Exploración y Preprocesamiento:
   - Utilizar los notebooks en `Exploracion_datos/` para entender y preprocesar los datos.
4. Entrenamiento de Modelos:
   - Los notebooks en `models_training/` contienen el proceso de selección y optimización de modelos.
5. Despliegue:
   - El modelo final entrenado se encuentra en `PROYECTO/models/Prediccion_score_c_rf.pkl` y puede ser cargado y utilizado como se muestra en `Ejemplo.py`.
   - La aplicación para el despliegue está implementada en `app.py` usando Streamlit.

## Contacto

Para más información o preguntas sobre este proyecto, puedes contactarme a través de felipe.espinoza1299@gmail.com.
