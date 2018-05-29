from flask import Flask
from flask import render_template, request
myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return "Welcome to my app!"

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)