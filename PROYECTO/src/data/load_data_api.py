import os
from kaggle.api.kaggle_api_extended import KaggleApi
import shutil
from dotenv import load_dotenv


load_dotenv()
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

api = KaggleApi()
api.authenticate()


dataset = 'parisrohan/credit-score-classification'
download_path = os.path.join('..', '..', 'data', 'raw')

if not os.path.exists(download_path):
    os.makedirs(download_path)

api.dataset_download_files(dataset, path=download_path, unzip=True)

files = os.listdir(download_path)
print("Archivos descargados:")
for file in files:
    print(file)

for file in files:
    if file.endswith('.csv'):
        shutil.move(os.path.join(download_path, file), download_path)
