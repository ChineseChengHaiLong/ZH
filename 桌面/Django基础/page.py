from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
...
class GoodsPagination(PageNumberPagination):
	page_size = 12
	page_size_query_param = 'page_size'
	page_query_param = "page"
	max_page_size = 100
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	商品列表页
	"""
	...
	# 分页
	pagination_class = GoodsPagination
