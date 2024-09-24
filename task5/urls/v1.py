from django.urls import path, include
from rest_framework.routers import DefaultRouter


from task5.views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
urlpatterns = [
    path('', include(router.urls))
]
