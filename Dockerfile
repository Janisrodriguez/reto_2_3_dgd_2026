FROM python:3.12-slim

WORKDIR /app

# (Opcional pero recomendado) pip actualizado
RUN pip install --no-cache-dir --upgrade pip

# Instala dependencias usando SOLO requirements.txt (mejor cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiamos el resto del proyecto (pero si usas volumes igual se “pisa” al correr)
COPY . /app

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=Reto2", "--ServerApp.password="]


