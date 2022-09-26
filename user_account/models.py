from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class RestaurantUser(AbstractUser):
    phone_number = PhoneNumberField(blank=False, null=False, unique=True)


