#!/usr/bin/python3
"""
Script to start a Flask Web application
Listening on port 0.0.0.0.0:5000
Displaying Hello HBNB!
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
