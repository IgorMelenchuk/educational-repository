import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def main():
    # Подключаемся к локальному серверу RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Убеждаемся, что очередь 'hello' существует
    channel.queue_declare(queue='hello')

    # Устанавливаем функцию обратного вызова на получение сообщений
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
