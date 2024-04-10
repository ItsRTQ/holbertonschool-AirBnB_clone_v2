#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home_page():
    """This method send the data for the homepage"""

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This method send the data for the hbnb route"""

    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
