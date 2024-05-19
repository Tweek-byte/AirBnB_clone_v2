#!/usr/bin/python3
#!/usr/bin/python3
''' Flask setup'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' Index function '''
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
