from django.db import models
from djmoney.models.fields import MoneyField


class Menu(models.Model):
    Available_Time = (
        ('lunch', 'Lunch 1pm - 4pm'),
        ('dinner', 'Dinner 6pm - 11pm'),
    )
    Ability_Today = (
        ('yes', 'Yes'),
        ('out-of-stock', 'Out Of Stock')
    )
    title = models.CharField(max_length=500)
    short_details = models.TextField()
    image = models.FileField(upload_to='menu/menu-images', default='menu/menu-images/default.png')
    available_time = models.CharField(max_length=30, choices=Available_Time)
    ability_today = models.CharField(max_length=30, choices=Ability_Today, default='yes')
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='BDT')

