# wsgi.py
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! 2"

@app.route('/api/v1/products')
def products():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'NewProduct' }
    ]
    return jsonify(PRODUCTS)

