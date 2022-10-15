from rest_framework import serializers

from order.models import Order


class OrderSerializers(serializers.ModelSerializer):

    order_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        order_by = Order.objects.create(order_by=self.context['request'].user, **validated_data)
        return order_by

    class Meta:
        model = Order
        fields = ('order_number', 'set_menu_number', 'created_at', 'order_status', 'order_by',)
        read_only_fields = ('order_status', )


class OrderUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_number', 'set_menu_number', 'order_status',)
        read_only_fields = ('order_number', 'set_menu_number', )
