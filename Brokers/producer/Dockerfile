# Dockerfile for Producer
FROM python:3.11-slim

# Устанавливаем необходимые зависимости
RUN pip install pika

# Копируем скрипт в контейнер
COPY producer.py /app/producer.py

# Переходим в рабочую директорию
WORKDIR /app

# Запускаем producer
CMD ["python", "producer.py"]
