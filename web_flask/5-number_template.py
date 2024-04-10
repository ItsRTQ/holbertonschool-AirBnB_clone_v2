#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask
from flask import render_template

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


@app.route("/c/<text>")
def c_text(text):
    """This method takes data from the url to print text"""

    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", defaults={"text": None})
@app.route("/python/<text>")
def python_text(text):
    """This method takes data from the url to print text with default value"""

    if text:
        text = text.replace("_", " ")
    else:
        text = "is cool"
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """This method creates a route with n  value if n is a number"""

    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    if isinstance(n, int):
        return render_template('templates/5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
