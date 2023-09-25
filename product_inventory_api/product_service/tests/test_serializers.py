from django.test import TestCase
from product_service.models import Product
from product_service.serializers import ProductSerializer

class ProductSerializerTest(TestCase):

    def setUp(self):
        self.product_attributes = {
            'name': 'Blue Shirt',
            'description': 'A stylish blue shirt.',
            'price': 19.99,
            'quantity': 5,
            'category': Product.CLOTHING,
        }
        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name', 'description', 'price', 'quantity', 'category'])

    def test_product_field_content(self):
        data = self.serializer.data
        for field in ['name', 'description', 'quantity', 'category']:
            self.assertEqual(data[field], self.product_attributes[field])
        self.assertEqual(data['price'], str(self.product_attributes['price']))

    def test_product_validation(self):
        serializer = ProductSerializer(data=self.product_attributes)
        self.assertTrue(serializer.is_valid())
