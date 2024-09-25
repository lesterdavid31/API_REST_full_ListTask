from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    completed = filters.BooleanFilter()
    class Meta:
        model = Task
        fields = ['title','completed']