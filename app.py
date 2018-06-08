from flask import Flask
from flask import render_template, request
from helpers.data import *

CENSUSTRACTS = get_tracts()

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return render_template('homepage.html', tracts=CENSUSTRACTS)


if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
