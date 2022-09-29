from rest_framework.viewsets import ModelViewSet

from menu.models import Menu
from menu.serializers import MenuSerializers, MenuUpdateSerializers


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    lookup_field = 'id'
