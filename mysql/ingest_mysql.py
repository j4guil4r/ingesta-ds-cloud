import pymysql
import pandas as pd
import boto3

# Conectar a la base de datos MySQL
connection = pymysql.connect(
    host='3.234.197.222',  # IP de la base de datos MySQL
    port=8007,  # Puerto expuesto en Docker para MySQL
    user='root',
    password='utec',
    database='MC_Estudiantes'
)

# Conectar a S3
s3 = boto3.client('s3')
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud-2'  # Reemplaza con el nombre de tu bucket

# Consulta para extraer registros de la tabla Estudiante
df_estudiantes = pd.read_sql("SELECT * FROM Estudiante", connection)
csv_file_estudiantes = "/tmp/estudiantes.csv"
df_estudiantes.to_csv(csv_file_estudiantes, index=False)
s3.upload_file(csv_file_estudiantes, bucket_name, 'microservicio1/estudiantes.csv')

# Consulta para extraer registros de la tabla Carrera
df_carreras = pd.read_sql("SELECT * FROM Carrera", connection)
csv_file_carreras = "/tmp/carreras.csv"
df_carreras.to_csv(csv_file_carreras, index=False)
s3.upload_file(csv_file_carreras, bucket_name, 'microservicio1/carreras.csv')

print("Datos de Estudiantes y Carreras cargados a S3 con éxito.")
