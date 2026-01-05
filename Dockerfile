FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "ingestor.py"]