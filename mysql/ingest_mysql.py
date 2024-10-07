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


# Consulta para extraer todos los registros
df = pd.read_sql("SELECT * FROM Estudiante", connection)

# Guardar los datos como CSV en un archivo temporal
csv_file = "/tmp/estudiantes.csv"
df.to_csv(csv_file, index=False)

# Conectar a S3
s3 = boto3.client('s3')

# Subir el archivo CSV al bucket S3
bucket_name = 'ingesta-aguilar-yoyi-ema-cloud-2'  # Reemplaza con el nombre de tu bucket
s3.upload_file(csv_file, bucket_name, 'microservicio1/estudiantes.csv')

print("Datos cargados a S3 con éxito.")
