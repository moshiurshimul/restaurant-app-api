from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class RestaurantUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=False, blank=False,)
    email = models.EmailField(_('Email'), unique=True, null=False, blank=False,)

    REQUIRED_FIELDS = ['phone_number', 'email']
