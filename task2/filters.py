import django_filters

from .models import Vacancy


class VacancyFilterBackend(django_filters.FilterSet):
    salary_from = django_filters.NumberFilter(field_name="salary", lookup_expr="gte")
    salary_to = django_filters.NumberFilter(field_name="salary", lookup_expr="lte")
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = ["salary_from", "salary_to", 'salary']
