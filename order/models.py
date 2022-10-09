from django.db import models
from django.contrib.auth import get_user_model
import random

User = get_user_model()


def random_string():
    return str(random.randint(10000, 99999))


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('order_in_queue', 'Order in queue'),
        ('order_accepted', 'Order accepted'),
        ('order_processing', 'Order processing'),
        ('order_delivered', 'Order delivered')
    )
    order_id = models.CharField(default=random_string, unique=True, editable=False, primary_key=True)
    set_menu_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=30, default='order_in_queue', choices=ORDER_STATUS_CHOICES)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
