# wsgi.py
from flask import Flask
from flask.json import jsonify
from flask import request

app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'NewProduct' }
]

def get_new_product_id():
    ids = [PRODUCTS[x]['id'] for x in range(len(PRODUCTS))]
    return int(sorted(ids)[-1]) + 1

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def products_read():

    return jsonify(PRODUCTS)

@app.route('/api/v1/products', methods=['POST'])
def products_create():
    product = request.form.get('name')
    PRODUCTS.append({'id': get_new_product_id(), 'name': product})
    return jsonify(PRODUCTS[-1])

@app.route('/api/v1/products/update', methods=['POST'])
def products_update():
    id = request.form.get('id')
    for idx in range(len(PRODUCTS)):
        if PRODUCTS[idx].get('id') == id:
            break
    product = request.form.get('name')
    PRODUCTS[idx]['name'] = product
    return jsonify(PRODUCTS[idx])

