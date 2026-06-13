# Usamos una versión ligera de Python
FROM python:3.11-slim

# Le decimos a Docker en qué carpeta trabajar dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos e instalamos las dependencias
# (AQUÍ NO USAMOS VENV, Docker ya aísla las cosas por sí mismo)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de nuestro proyecto al contenedor
COPY . .

# Comando para arrancar FastAPI con recarga automática
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
