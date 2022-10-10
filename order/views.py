from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from order.models import Order


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

