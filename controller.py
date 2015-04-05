import gevent
import utils

from flask import Flask, render_template
from gevent import wsgi

app = Flask(__name__)
app.secret_key = "key"


@app.route("/fib/<int:n>")
def get_fib_value(n):
    fib_value = utils.get_fibonacci(n)
    print fib_value
    return render_template("fib.html", fib_value = fib_value)

server = wsgi.WSGIServer(('127.0.0.1', 8000),app)
server.serve_forever()
