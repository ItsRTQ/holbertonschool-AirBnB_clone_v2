#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask
from flask import render_template
from models import storage
from os import getenv


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route("/")
def home_page():
    """This method send the data for the homepage"""

    return "Hello HBNB!"


@app.teardown_appcontext
def close_storage():
    """This method closes storage session if storage db"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


@app.route("/states_list")
def state_list():
    """This method fetchs data from storage to display the list of states"""

    states = storage.all("State")
    data_to_sort = {}
    for key, value in states.items():
        data_to_sort[value["name"]] = value["id"]
    sorted_data = dict(sorted(data_to_sort.items()))
    return render_template("7-states_list.html", states=sorted_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
