#!/usr/bin/python3
"""This module will start a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State, City
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """This method will close the SQLAlchemy session on teardown"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters_html():
    """Display flask web application, based on storage fetch data"""

    states = storage.all(State)
    return render_template("10-hbnb_filters.html", state=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
