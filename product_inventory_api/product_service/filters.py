import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    """
    FilterSet for filtering Product instances based on specific criteria.

    Attributes:
    - name: Filters by product name with a case-insensitive containment search.
    - min_price: Filters products with a price greater than or equal to this value.
    - max_price: Filters products with a price less than or equal to this value.
    - category: Filters products based on given category or categories.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.MultipleChoiceFilter(choices=Product.CATEGORY_CHOICES)
    class Meta:
        model = Product
        fields = ['name', 'min_price', 'max_price', 'category']
