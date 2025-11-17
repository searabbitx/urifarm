from flask import Flask, request, render_template
import redis
import hashlib
app = Flask(__name__)

pool = redis.ConnectionPool().from_url("redis://redis")

def send_path(path):
    with redis.Redis().from_pool(pool) as r:
        r.sadd("paths", path)

def get_template_name_by(path):
    temps = [
        'apache.html',
        'iis_4.html',
        'landing1.html',
        'landing2.html',
        'nginx.html',
        'tomcat.html',

        'SORRY',
        'NOT',
        'TODAY',
    ]
    somehex = hashlib.md5(path.encode()).hexdigest()[0:4]
    return temps[int(somehex, 16) % len(temps)]




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    url = request.url[len(request.url_root)-1:]
    send_path(url)
    templ = get_template_name_by(path)
    if templ.endswith('.html'):
        return render_template(templ)
    else:
        return "Not found", 404


if __name__ == '__main__':
    app.run()

