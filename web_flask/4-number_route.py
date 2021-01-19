#!/usr/bin/python3
""" minimal Flask application
    that return a string """


from flask import Flask
from flask import abort

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


if __name__ == '__main__':
    app.run()
