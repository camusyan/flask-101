# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_read_all(self):
        print("\nTEST_PRODUCTS_READ_ALL", flush=True)
        response = self.client.get("/api/v1/products")
        products = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        self.assertEqual(response.status_code, 200)

    def test_products_read(self):
        print("\nTEST_PRODUCTS_READ", flush=True)
        response = self.client.get("/api/v1/products/2")
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 2)
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/api/v1/products/10")
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        #self.assertIsInstance(product, dict)
        self.assertEqual(response.status_code, 404)

    def test_product_create(self):
        print("\nTEST_PRODUCT_CREATE", flush=True)
        response = self.client.post("/api/v1/products", data={"name": "Star Wars"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 4)
        self.assertEqual(product['name'], "Star Wars")
        self.assertEqual(response.status_code, 201)

    def test_product_update(self):
        print("\nTEST_PRODUCT_UPDATE", flush=True)
        response = self.client.patch("/api/v1/products/3", data={"name": "Star Trek"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 3)
        self.assertEqual(product['name'], "Star Trek")
        self.assertEqual(response.status_code, 200)

        response = self.client.patch("/api/v1/products/10", data={"name": "bad id"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        self.assertEqual(response.status_code, 422)

    def test_product_delete(self):
        print("\nTEST_PRODUCT_DELETE", flush=True)
        response = self.client.delete("/api/v1/products/1")
        product = response.json
        print(response.status_code, flush=True)
        #self.assertIsInstance(product, dict)
        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/api/v1/products/10")
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        self.assertEqual(response.status_code, 422)

