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
def products_read():
    form = request.form
    if len(form) == 0:
        return jsonify(PRODUCTS), 200
    elif 'name' in form.keys():
        idx = get_product_index_from_name(form.get('name'))
        if idx is not None:
            id = PRODUCTS[idx].get('id')
            name = PRODUCTS[idx].get('name')
            return jsonify({'id': id, 'name': name}), 200
        else:
            return "", 404
    else:
        return "", 400

@app.route('/api/v1/products', methods=['POST'])
def products_create():
    product = request.form.get('name')
    PRODUCTS.append({'id': get_new_product_id(), 'name': product})
    return jsonify(PRODUCTS[-1]), 201

@app.route('/api/v1/products/update', methods=['POST'])
def products_update():
    form = request.form
    if 'id' not in form.keys() or 'name' not in form.keys():
        return "", 400

    id = form.get('id')
    name = form.get('name')
    idx = get_product_index_from_id(id)
    if idx is not None:
        PRODUCTS[idx]['name'] = name
        return jsonify(PRODUCTS[idx]), 200
    else:
        return "", 404

@app.route('/api/v1/products/delete', methods=['POST'])
def products_delete():
    product = request.form.get('name')
    idx = get_product_index_from_name(product)

    if idx is not None:
        del PRODUCTS[idx]
        return "", 204

    return "", 404
