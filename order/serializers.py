from rest_framework import serializers

from order.models import Order


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('set_menu_number', )


class OrderUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_status', )
