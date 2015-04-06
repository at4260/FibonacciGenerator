import utils

from flask import Flask, render_template
from gevent import wsgi

app = Flask(__name__)
app.secret_key = "key"


@app.route("/fib/<n>")
def get_fib_value(n):
    """
    Calculates the nth value in the fibonacci sequence.

    Uses try and except to check if the user inputted value can
    be converted to an integer. Floats and strings cannot be
    converted, so will error out and return "Not valid."
    """
    try:
        fib_value = utils.get_fibonacci(int(n))
        return render_template("fib.html", fib_value=fib_value)
    except:
        return "Not valid"

server = wsgi.WSGIServer(('127.0.0.1', 8000), app)
server.serve_forever()
