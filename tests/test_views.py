# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_product_create(self):
        response = self.client.post("/api/v1/products", data={"name": "Star Wars"})
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 4)
        self.assertEqual(product['name'], "Star Wars")

    def test_product_update(self):
        response = self.client.post("/api/v1/products/update", data={"id": 4, "name": "Star Trek"})
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 4)
        self.assertEqual(product['name'], "Star Trek")
