from decimal import Decimal

from rest_framework.test import APITestCase

from product_service.models import Product

# Create your tests here.
class ProductQueryTests(APITestCase):
    fixtures = ['initial_products.json']

    def test_filter_products_by_price_range(self):
        """
        Test to ensure that when querying the product list endpoint with min_price and max_price filters, 
        it returns all the products within the specified price range.
        """
        min_price = 50
        max_price = 250

        params = {
            'min_price': min_price,
            'max_price': max_price
        }

        response = self.client.get('/products/', data=params)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data['count'], 1)

        # Ensure the response data the price is within range
        for product_data in response.data['results']:
            self.assertGreaterEqual(Decimal(product_data['price']), min_price)
            self.assertLessEqual(Decimal(product_data['price']), max_price)

    def test_filter_products_by_multiple_categories(self):
        """
        Test to ensure that when querying the product list endpoint with multiple category filters, 
        it returns all the products that belong to either of the specified categories.
        """
        category1 = Product.ELECTRONICS
        category2 = Product.CLOTHING

        params = {
            'category': [category1, category2]
        }

        response = self.client.get('/products/', data=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 10)

        # Ensure the response data has products from either of the specified categories
        for product_data in response.data['results']:
            self.assertIn(product_data['category'], [category1, category2])
