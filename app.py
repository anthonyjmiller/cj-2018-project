from flask import Flask
from flask import render_template, request
from helpers.data import *

CENSUSTRACTS = get_tracts()
CRIMES_GEOPATH = get_crimes()

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return render_template('homepage.html', tracts=CENSUSTRACTS, crimes=CRIMES_GEOPATH)

@myapp.route("/entity")
def entity():
    return render_template('entity.html', tracts=CENSUSTRACTS, crimes=CRIMES_GEOPATH)


if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
