#!/usr/bin/python3
"""
Display “Python ” and value of the text variable
replace underscore _ symbols with a space
The default value of text is “is cool”
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display "C" followed by value of test"""
    return "C " + text.replace("_", " ")


@app.route('python/', strict_slashes=False)
@app.route('python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the text variable value"""
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
