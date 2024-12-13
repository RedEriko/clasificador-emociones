# Utilizamos una imagen base de Python (en este caso, Python 3.9)
FROM python:3.10

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt a la imagen
COPY requirements.txt .

# Copia el contenido del directorio actual en el contenedor en /app
COPY ./api /app

# Instalamos las dependencias de la aplicación desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto que usará la aplicación (FastAPI por defecto usa el puerto 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación utilizando uvicorn (servidor ASGI)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

