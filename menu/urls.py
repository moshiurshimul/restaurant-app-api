from django.urls import path, include
from rest_framework import routers

from menu.views import MenuViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
