import pika

def main():
    # Подключаемся к серверу RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Создаем очередь 'hello'
    channel.queue_declare(queue='hello')

    # Отправляем сообщение
    message = "Hello, RabbitMQ!"
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f" [x] Sent '{message}'")

    # Закрываем соединение
    connection.close()

if __name__ == "__main__":
    main()
