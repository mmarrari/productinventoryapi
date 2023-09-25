from django.test import TestCase
from product_service.models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=9.99,
            quantity=5,
            category=Product.ELECTRONICS
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(str(self.product), "Test Product - $9.99 (Electronics)")

    def test_default_category(self):
        self.assertEqual(self.product.category, Product.ELECTRONICS)

    def test_str_method(self):
        expected_string_representation = "Test Product - $9.99 (Electronics)"
        self.assertEqual(str(self.product), expected_string_representation)


