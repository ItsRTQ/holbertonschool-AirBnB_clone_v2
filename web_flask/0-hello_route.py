#!/usr/bin/python3
""" This modules creates a super basic flask local server """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_page():
    """This method just returns simple text"""

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
