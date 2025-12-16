from django_filters import filterset
from django_filters.rest_framework import  filters

class Filterexpense (filterset.FilterSet) : 
    search = filters.CharFilter(field_name= "fullname" , lookup_expr='icontains') 
    max_amount = filters.NumberFilter(field_name="amount" , lookup_expr='gte')
    min_amount = filters.NumberFilter(field_name="amount" , lookup_expr='lte')
    category_id = filters.NumberFilter(field_name="category_id" , lookup_expr='exact')
