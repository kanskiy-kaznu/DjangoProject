import django_filters
from .models import Task_Models
from django import forms


class TaskSearchParametr(django_filters.FilterSet):
    class Meta:
        model = Task_Models
        fields = '__all__'
