# to help in search
import django_filters
from .models import *
# class DollFilter(django_filters.FilterSet):
#     name_of_the_doll = django_filters.CharFilter(lookup_expr='icontains', label='Doll Name')

#     class Meta:
#         model = "Doll"
#         fields = []

# class Category_dollFilter(django_filters.FilterSet):
#     class Meta: 
#         model=Category_doll
#         fields=['name']   

class DollFilter(django_filters.FilterSet):

    class Meta:
        model = Doll
        fields = ['name_of_the_doll']