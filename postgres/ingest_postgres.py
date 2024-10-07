import psycopg2
import pandas as pd
import boto3

# Conectar a la base de datos PostgreSQL
connection = psycopg2.connect(
    host='3.234.197.222',
    port=8006,  # Puerto expuesto en Docker para PostgreSQL
    user='postgres',
    password='utec',
    database='MS_Cursos'
)

# Conectar a S3
s3 = boto3.client('s3')
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud-2'  # Reemplaza con el nombre de tu bucket

# Consulta para extraer registros de la tabla Curso
df_cursos = pd.read_sql("SELECT * FROM Curso", connection)
csv_file_cursos = "/tmp/cursos.csv"
df_cursos.to_csv(csv_file_cursos, index=False)
s3.upload_file(csv_file_cursos, bucket_name, 'microservicio2/cursos.csv')

# Consulta para extraer registros de la tabla Profesor
df_profesores = pd.read_sql("SELECT * FROM Profesor", connection)
csv_file_profesores = "/tmp/profesores.csv"
df_profesores.to_csv(csv_file_profesores, index=False)
s3.upload_file(csv_file_profesores, bucket_name, 'microservicio2/profesores.csv')

print("Datos de Cursos y Profesores cargados a S3 con éxito.")
