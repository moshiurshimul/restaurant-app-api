from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

from order.models import Order
from order.serializers import OrderSerializers, OrderUpdateSerializers


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_classes = {
        'update': OrderUpdateSerializers,
        'partial_update': OrderUpdateSerializers,
    }

    default_serializer_class = OrderSerializers
    lookup_field = 'order_number'
    filter_backends = (SearchFilter, )
    search_fields = ['order_status', ]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        if self.action in ['list', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]

        elif self.action in ['create', 'retrieve']:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



