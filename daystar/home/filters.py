# to help in search
import django_filters
from .models import *
class ProductFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='icontains', label='Product Name')

    class Meta:
        model = "Product"
        fields = []
        