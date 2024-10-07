from pymongo import MongoClient
import pandas as pd
import boto3

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb://3.234.197.222:27017/MS_Evaluaciones')
db = client['MS_Evaluaciones']

# Conectar a S3
s3 = boto3.client('s3')
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud-2'  # Reemplaza con el nombre de tu bucket

# Extraer datos de la colección Evaluacion
df_evaluaciones = pd.DataFrame(list(db['Evaluacion'].find()))
csv_file_evaluaciones = "/tmp/evaluaciones.csv"
df_evaluaciones.to_csv(csv_file_evaluaciones, index=False)
s3.upload_file(csv_file_evaluaciones, bucket_name, 'microservicio3/evaluaciones.csv')

# Extraer datos de la colección Notas
df_notas = pd.DataFrame(list(db['Notas'].find()))
csv_file_notas = "/tmp/notas.csv"
df_notas.to_csv(csv_file_notas, index=False)
s3.upload_file(csv_file_notas, bucket_name, 'microservicio3/notas.csv')

print("Datos de Evaluaciones y Notas cargados a S3 con éxito.")
