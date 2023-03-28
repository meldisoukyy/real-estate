from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_ROLE = (('buyer', 'Buyer'), ('seller', 'Seller'))


class User(AbstractUser):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=USER_ROLE)
    USERNAME_FIELD = 'national_id'
    REQUIRED_FIELDS = ['name', 'email', 'phone', 'role']
