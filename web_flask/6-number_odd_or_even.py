#!/usr/bin/python3
""" minimal Flask application
    that return a string """


from flask import Flask
from flask import abort
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    """ main route """

    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    """ hbnb directory """

    return "HBNB"


@app.route("/c/<text>")
def c_dir(text):
    """
    Return C and the value of var 'text'
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python/<text>")
@app.route("/python/")
def python_dir(text="is cool"):
    """
    Return python and the value of var 'text'
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<n>")
def number(n):
    """
    Returns n, if n is an integer
    """
    try:
        return ("{} is a number".format(int(n)))
    except Exception:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        abort(404)


@app.route("/number_odd_or_even/<n>")
def number_odd_or_even_template(n):
    """
     display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    try:
        n = int(n)
        if n % 2 == 0:
            s = "even"
        else:
            s = "odd"
        return render_template('6-number_odd_or_even.html', n=n, s=s)
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run()
