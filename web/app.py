from flask import Flask, request
app = Flask(__name__)

def send_path(path):
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='paths')

    channel.basic_publish(exchange='', routing_key='paths', body=path)
    connection.close()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    url = request.url[len(request.url_root)-1:]
    send_path(url)
    return f'Url: {url}\n'


if __name__ == '__main__':
    app.run()

