# to help in search
import django_filters
from .models import *
class DollFilter(django_filters.FilterSet):
    doll_name = django_filters.CharFilter(lookup_expr='icontains', label='Doll Name')

    class Meta:
        model = "Doll"
        fields = []

# class CategoryFilter(django_filters.FilterSet):
#     class Meta: 
#         model=Category
#         fields=['name']   