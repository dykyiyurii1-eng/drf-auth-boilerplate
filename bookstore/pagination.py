from rest_framework.pagination import PageNumberPagination


class RoleBasedPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_page_size(self, request):
        if request.user and request.user.is_authenticated:
            return 20
        return 5