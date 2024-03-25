from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'pagesize'
    max_page_size = 100

    def __init__(self, *args, **kwargs):
        page_size = kwargs.pop('page_size', None)
        super().__init__(*args, **kwargs)
        if page_size is not None:
            self.page_size = page_size
