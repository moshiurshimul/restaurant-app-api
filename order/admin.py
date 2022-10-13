from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'set_menu_number', 'created_at', 'order_status', )
    list_filter = ('order_status', )

