from django.urls import path, include
from rest_framework.routers import DefaultRouter


from task3.views import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
urlpatterns = [
    path('', include(router.urls))
]
