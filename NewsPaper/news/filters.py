import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    data = DateTimeFilter(field_name='time_create',
                          lookup_expr='lt',
                          label='Date',
                          widget=DateTimeInput(attrs={'type': 'date'}, format='%Y-%m-%dT',),)

    class Meta:
        model = Post
        fields = {"title": ['icontains'], "category": ['exact'] }


class NWFilter(FilterSet):
    pass


class ARFilter(FilterSet):
    pass