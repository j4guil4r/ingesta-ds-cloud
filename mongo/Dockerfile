FROM python:3.9

# Instalar las dependencias necesarias
RUN pip install pandas pymongo boto3

# Copiar el script de ingesta al contenedor
COPY ingest_mongo.py /app/ingest_mongo.py

# Configurar el punto de entrada
CMD ["python", "/app/ingest_mongo.py"]
