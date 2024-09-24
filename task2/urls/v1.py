from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task1.views import UserViewSet
from task2.views import VacancyViewSet

router = DefaultRouter()
router.register(r'vacancy', VacancyViewSet, basename='vacancy')
urlpatterns = [
    path('', include(router.urls))
]
