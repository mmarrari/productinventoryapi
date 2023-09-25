from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Represents a product in our inventory.

    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (decimal): The price of the product.
        quantity (int): The quantity of the product in stock.
        category (str): The category to which the product belongs (e.g., Electronics, Clothing, Food).
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    ELECTRONICS = 'Electronics'
    CLOTHING = 'Clothing'
    FOOD = 'Food'
    CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (FOOD, 'Food'),
    ]
    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        default=ELECTRONICS,
    )

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='idx_product_name'),
            models.Index(fields=['price'], name='idx_product_price'),
            models.Index(fields=['category'], name='idx_product_category'),
            models.Index(fields=['category', 'price', 'name'], name='idx_product_cat_price_name'),
        ]

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.get_category_display()})"