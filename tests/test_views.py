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
        response = self.client.get("/api/v1/products", data={"name": "Socialive.tv"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 2)
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/api/v1/products", data={"name": "toto"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        #self.assertIsInstance(product, dict)
        self.assertEqual(response.status_code, 404)

        response = self.client.get("/api/v1/products", data={"badkey": "_"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        self.assertEqual(response.status_code, 400)

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
        response = self.client.post("/api/v1/products/update", data={"id": 3, "name": "Star Trek"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 3)
        self.assertEqual(product['name'], "Star Trek")
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/api/v1/products/update", data={"id": 10, "name": "bad id"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        self.assertEqual(response.status_code, 404)

        response = self.client.post("/api/v1/products/update", data={"bad_key": 10, "bad_name": "bad name"})
        product = response.json
        print(response.status_code, flush=True)
        self.assertIsNone(product)
        self.assertEqual(response.status_code, 400)

    def test_product_delete(self):
        print("\nTEST_PRODUCT_DELETE", flush=True)
        response = self.client.post("/api/v1/products/delete", data={"name": "Skello"})
        product = response.json
        print(response.status_code, flush=True)
        #self.assertIsInstance(product, dict)
        self.assertEqual(response.status_code, 204)

