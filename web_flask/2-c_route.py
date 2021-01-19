#!/usr/bin/python3
""" minimal Flask application
    that return a string """


from flask import Flask

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


if __name__ == '__main__':
    app.run()
