from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrafficDataViewSet

router = DefaultRouter()
router.register(r'traffic-data', TrafficDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
