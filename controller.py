import gevent
import utils

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "key"


@app.route("/fib/<int:n>")
def get_fib_value(n):
    fib_value = utils.get_fibonacci(n)
    print fib_value
    return render_template("fib.html", fib_value = fib_value)


if __name__ == "__main__":
    app.run(debug=True)
