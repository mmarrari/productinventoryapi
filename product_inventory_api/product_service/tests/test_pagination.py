from rest_framework.test import APITestCase

from product_service.models import Product

# Create your tests here.
class ProductQueryTests(APITestCase):
    fixtures = ['initial_products.json']
    
    def test_pagination_with_category_filtering(self):
        """
        Test to ensure that when querying the product list endpoint with category filters
        and pagination parameters, the API returns the expected subset of products.
        """
        # Set up filter and pagination parameters
        categories_to_filter = [Product.ELECTRONICS, Product.FOOD]
        page_size = 5
        page_number = 2

        params = {
            'category': categories_to_filter,
            'page_size': page_size,
            'page': page_number
        }

        response = self.client.get('/products/', data=params)
        self.assertEqual(response.status_code, 200)

        # Ensure the response data contains products of the desired categories
        for product_data in response.data['results']:
            self.assertIn(product_data['category'], categories_to_filter)

        self.assertEqual(len(response.data['results']), page_size)
