FROM python:3.9

# Instalar las dependencias necesarias
RUN pip install pandas psycopg2 boto3

# Copiar el script de ingesta al contenedor
COPY ingest_postgres.py /app/ingest_postgres.py

# Configurar el punto de entrada
CMD ["python", "/app/ingest_postgres.py"]
