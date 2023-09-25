from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer is used to transform Product model instances into JSON data and vice versa.
    It defines the fields to be serialized and provides validation for incoming data.

    Attributes:
        id (int): The unique identifier of the product.
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (decimal): The price of the product.
        quantity (int): The quantity of the product in stock.
        category (str): The category to which the product belongs (e.g., Electronics, Clothing, Food).
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'category']