from rest_framework.pagination import CursorPagination

class MyCursorPagnition(CursorPagination):
   page_size = 5
   ordering = 'name'
   #cursor_query_param='cu'