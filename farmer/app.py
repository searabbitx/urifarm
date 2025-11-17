import pika, sys, os, time

def connect():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
        print(" [x] Connected")
        return connection
    except pika.exceptions.AMQPConnectionError:
        print(" [x] Connection failed, reconnecting")
        time.sleep(1)
        return connect()


def main():
    connection = connect()
    channel = connection.channel()

    channel.queue_declare(queue='paths')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='paths', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
