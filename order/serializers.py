from rest_framework import serializers

from order.models import Order


class OrderSerializers(serializers.ModelSerializer):

    order_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        order = Order.objects.create(order_by=self.context['request'].user, **validated_data)
        return order

    class Meta:
        model = Order
        fields = ('set_menu_number', 'order_by', )


class OrderUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_status', )
