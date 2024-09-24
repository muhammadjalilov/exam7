from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from task2.filters import VacancyFilterBackend
from task2.models import Vacancy
from task2.serializers import VacancySerializer


class VacancyViewSet(ModelViewSet):
    """Custom Filter yozildi"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilterBackend
