from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from menu.models import Menu
from menu.serializers import MenuSerializers, MenuUpdateSerializers


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_classes = {
        'update': MenuUpdateSerializers,
        'partial_update': MenuUpdateSerializers,
    }
    default_serializer_class = MenuSerializers
    lookup_field = 'id'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance=instance, validated_data=serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


