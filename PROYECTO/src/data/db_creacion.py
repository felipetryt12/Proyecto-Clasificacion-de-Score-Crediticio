import os
import sqlite3
import pandas as pd

# Obtener la ruta del directorio donde está ubicado el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define las rutas relativas basadas en el directorio del script
database_path = os.path.join(script_dir, 'database_credito.db')  # La base de datos está en 'src\data'
train_csv_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'train.csv')  # Desde 'src\data' a 'data\raw'
test_csv_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'test.csv')   # Desde 'src\data' a 'data\raw'


print(f"Ruta absoluta de la base de datos: {database_path}")
print(f"Ruta absoluta de train.csv: {train_csv_path}")
print(f"Ruta absoluta de test.csv: {test_csv_path}")


if not os.path.exists(train_csv_path):
    raise FileNotFoundError(f"El archivo {train_csv_path} no existe.")
if not os.path.exists(test_csv_path):
    raise FileNotFoundError(f"El archivo {test_csv_path} no existe.")

conn = sqlite3.connect(database_path)
cursor = conn.cursor()


data_train = pd.read_csv(train_csv_path)
data_test = pd.read_csv(test_csv_path)

data_train.to_sql('training_set', conn, if_exists='replace', index=False)
data_test.to_sql('testing_set', conn, if_exists='replace', index=False)

conn.commit()

conn.close()
