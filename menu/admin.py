from django.contrib import admin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_details', 'available_time', 'ability_today', 'price', )
    list_filter = ('available_time', 'ability_today', )
