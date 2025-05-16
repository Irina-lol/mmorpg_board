import django_filters
from .models import Response

class ResponseFilter(django_filters.FilterSet):
    class Meta:
        model = Response
        fields = ['ad__category']