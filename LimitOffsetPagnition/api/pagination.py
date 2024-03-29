from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 5
   limit_query_param = 'myl'
   offset_query_param = 'off'
   max_limit = 6