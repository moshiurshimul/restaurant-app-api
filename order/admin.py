from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'set_menu_number', 'created_at', 'order_status', )

