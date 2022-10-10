from django.urls import path, include
from rest_framework import routers

from order.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]

