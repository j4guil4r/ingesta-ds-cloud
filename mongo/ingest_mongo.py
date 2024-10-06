import pandas as pd
import boto3
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb://3.234.197.222:27017/')
db = client['MS_Evaluaciones']

# Extraer los documentos de la colección Evaluaciones
evaluaciones = db.Evaluaciones.find()
df = pd.DataFrame(list(evaluaciones))

# Guardar los datos como CSV en un archivo temporal
csv_file = "/tmp/evaluaciones.csv"
df.to_csv(csv_file, index=False)

# Conectar a S3
s3 = boto3.client('s3')

# Subir el archivo CSV al bucket S3
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud'  # Reemplaza con el nombre de tu bucket
s3.upload_file(csv_file, bucket_name, 'microservicio3/evaluaciones.csv')

print("Datos cargados a S3 con éxito.")
