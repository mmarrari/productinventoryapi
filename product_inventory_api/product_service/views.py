from rest_framework import generics

from .filters import ProductFilter
from .models import Product
from .pagination import CustomPagination
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    """
    API view to list all products based on specific filter criteria.

    Example usage:
    GET /products/?name=lue&min_price=50&max_price=1000&category=Clothing

    This would return a list of products with names containing "lue", 
    category "Clothing" and prices ranging from 50 to 1000.
    
    Filters:
    - name: Filters by product name with a case-insensitive containment search.
    - min_price: Filters products with a price greater than or equal to this value.
    - max_price: Filters products with a price less than or equal to this value.
    - category: Filters products based on given category or categories.
    
    Pagination Usage Examples:

    - /products/?page=2: Retrieves the second page of products.
    - /products/?page_size=5: Retrieves products with a page size of 5.
    - /products/?min_price=10&max_price=1000&page=2&page_size=5: 
      Retrieves the second page of filtered products with a page size of 5.
    """
    queryset = Product.objects.all().order_by('category','name','price')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter 
    pagination_class = CustomPagination
