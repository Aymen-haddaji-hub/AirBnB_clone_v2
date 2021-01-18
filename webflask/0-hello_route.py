#!/usr/bin/python3
""" minimal Flask application 
    that return a string"""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    """ main route """

    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
