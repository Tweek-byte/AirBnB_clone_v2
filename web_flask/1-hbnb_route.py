#!/usr/bin/python3
""" Start the application"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return hello hbnb"""
  
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return HBNB function"""
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
