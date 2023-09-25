from rest_framework.test import APITestCase

from product_service.models import Product


# Create your tests here.
class ProductQueryTests(APITestCase):
    fixtures = ['initial_products.json']

    def test_retrieve_all_products(self):
        """
        Test to ensure that when querying the product list endpoint without filters, 
        it returns all the products in the database (in this case, 15 products) 
        and that the data structure is consistent with the expected serializer output.
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 15)

        # Ensure the response data contains the expected fields
        for product_data in response.data['results']:
            self.assertIn('id', product_data)
            self.assertIn('name', product_data)
            self.assertIn('description', product_data)
            self.assertIn('price', product_data)
            self.assertIn('quantity', product_data)
            self.assertIn('category', product_data)

    def test_post_method_not_allowed(self):
        """
        Test to ensure that the product list endpoint does not allow POST requests.
        """
        product_data = {
            'name': 'New Product',
            'description': 'A brand new product.',
            'price': 19.99,
            'quantity': 10,
            'category': Product.ELECTRONICS,
        }
        response = self.client.post('/products/', product_data, format='json')
        self.assertEqual(response.status_code, 405)
