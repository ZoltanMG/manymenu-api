# Usa la imagen de Python 3.9 como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Crear ambiente virtual
RUN python -m venv env

# Activar ambiente virtual
RUN . env/bin/activate

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo en la imagen de Docker
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta la aplicación
CMD ["python3", "-m", "api.app"]
