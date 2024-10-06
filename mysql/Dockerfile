FROM python:3.9

# Instalar las dependencias necesarias
RUN pip install pandas pymysql boto3

# Copiar el script de ingesta al contenedor
COPY ingest_mysql.py /app/ingest_mysql.py

# Configurar el punto de entrada
CMD ["python", "/app/ingest_mysql.py"]
