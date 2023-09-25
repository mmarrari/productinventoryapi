from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    """
    Custom pagination class that extends the default PageNumberPagination.

    Provides a default page size of 50 items and allows clients to specify 
    a custom page size using the `page_size` query parameter, up to a maximum of 10,000 items.

    Attributes:
    - page_size (int): The default number of items to include per page.
    - page_size_query_param (str): The name of the query parameter that clients can use
                                  to specify the number of items per page.
    - max_page_size (int): The maximum number of items that can be requested per page.

    Usage:
    In a view, set the pagination_class attribute to use this custom pagination:

    class SomeListView(generics.ListAPIView):
        pagination_class = CustomPagination
        ...

    Clients can use the `page_size` query parameter to adjust the number of items returned:

    - `/some-endpoint/`: By default, returns 50 items per page.
    - `/some-endpoint/?page_size=100`: Returns 100 items.
    - `/some-endpoint/?page_size=11000`: Returns a maximum of 10,000 items, as this is the set limit.

    """
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 10000