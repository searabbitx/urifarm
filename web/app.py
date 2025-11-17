from flask import Flask, request
import redis
app = Flask(__name__)

pool = redis.ConnectionPool().from_url("redis://redis")

def send_path(path):
    with redis.Redis().from_pool(pool) as r:
        r.sadd("paths", path)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    url = request.url[len(request.url_root)-1:]
    send_path(url)
    return f'Url: {url}\n'


if __name__ == '__main__':
    app.run()

