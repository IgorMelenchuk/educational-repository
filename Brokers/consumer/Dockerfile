# Dockerfile for Consumer
FROM python:3.11-slim

# Устанавливаем необходимые зависимости
RUN pip install pika

# Копируем скрипт в контейнер
COPY consumer.py /app/consumer.py

# Переходим в рабочую директорию
WORKDIR /app

# Запускаем consumer
CMD ["python", "consumer.py"]
