#!/usr/bin/python3
from flask import Flask
""" This modules creates a super basic flask local server """


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hbnb():
    """This method just returns simple text"""

    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
