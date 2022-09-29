from rest_framework import serializers

from menu.models import Menu


class MenuSerializers(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class MenuUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('available_time', 'ability_today')
