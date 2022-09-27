from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class RestaurantUser(AbstractUser):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(_('Email'), blank=False, unique=True)

    USERNAME_FIELD = 'phone_number'




