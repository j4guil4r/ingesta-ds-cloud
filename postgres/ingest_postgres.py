import psycopg2
import pandas as pd
import boto3

# Conectar a la base de datos PostgreSQL
connection = psycopg2.connect(
    host='3.234.197.222',  # IP de la base de datos PostgreSQL
    user='postgres',
    password='mypassword',
    database='MS_Cursos'
)

# Consulta para extraer los datos de la tabla Curso
df = pd.read_sql("SELECT * FROM Curso", connection)

# Guardar los datos como CSV en un archivo temporal
csv_file = "/tmp/cursos.csv"
df.to_csv(csv_file, index=False)

# Conectar a S3
s3 = boto3.client('s3')

# Subir el archivo CSV al bucket S3
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud'  # Reemplaza con el nombre de tu bucket
s3.upload_file(csv_file, bucket_name, 'microservicio2/cursos.csv')

print("Datos cargados a S3 con éxito.")
