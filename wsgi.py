# wsgi.py
from flask import Flask
from flask import jsonify
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

def get_product_index_from_name(name):
    for idx in range(len(PRODUCTS)):
        if PRODUCTS[idx].get('name') == name:
            return idx
    return None

def get_product_index_from_id(id):
    for idx in range(len(PRODUCTS)):
        if PRODUCTS[idx].get('id') == int(id):
            return idx
    return None

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def products_read_all():
    return jsonify(PRODUCTS), 200

@app.route('/api/v1/products/<id>', methods=['GET'])
def products_read(id):
    idx = get_product_index_from_id(int(id))
    if idx is not None:
        name = PRODUCTS[idx].get('name')
        return jsonify({'id': int(id), 'name': name}), 200
    else:
        return "", 404

@app.route('/api/v1/products', methods=['POST'])
def products_create():
    product = request.form.get('name')
    PRODUCTS.append({'id': get_new_product_id(), 'name': product})
    return jsonify(PRODUCTS[-1]), 201

@app.route('/api/v1/products/<id>', methods=['PATCH'])
def products_update(id):
    form = request.form

    if 'name' not in form.keys():
        return "", 400

    name = form.get('name')
    idx = get_product_index_from_id(int(id))
    if idx is not None:
        PRODUCTS[idx]['name'] = name
        return jsonify(PRODUCTS[idx]), 200
    else:
        return "", 422

@app.route('/api/v1/products/<id>', methods=['DELETE'])
def products_delete(id):
    idx = get_product_index_from_id(int(id))
    if idx is not None:
        del PRODUCTS[idx]
        return "", 204

    return "", 422
