
# Imagen base de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Evitar archivos .pyc y mostrar logs inmediatamente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copiar e instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto Django
COPY ejemplo/ .

# Crear directorio para la base de datos
RUN mkdir -p /data

# Puerto de Django
EXPOSE 8000

# Arrancar Django con Gunicorn
CMD ["gunicorn", "ejemplo.wsgi:application", "--bind", "0.0.0.0:8000"]
