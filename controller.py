import gevent
import utils

from flask import Flask, render_template
from gevent import wsgi

app = Flask(__name__)
app.secret_key = "key"


@app.route("/fib/<n>")
def get_fib_value(n):
    try:
        fib_value = utils.get_fibonacci(int(n))
        print fib_value
        return render_template("fib.html", fib_value=fib_value)
    except:
        return "Not valid"

server = wsgi.WSGIServer(('127.0.0.1', 8000), app)
server.serve_forever()
