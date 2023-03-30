from django.db import models
from accounts.models import User

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class JoinUsForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.TextField()

    def __str__(self):
        return self.name


# class Categories(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Usages(models.Model):
#     name = models.CharField(max_length=100)
#
#
# BUILDING_TYPES = (('1','1'),)
# BUILDING_CATEGORY = (('1','1'),)
# BUILDING_USAGE = (('1','1'),)
# OFFERS = (('1','1'),)
# PAYMENT_METHODS = (('1','1'),)
# REGIONS = (('1','1'),)
# CITIES = (('1','1'),)
# NEIGHBORHOODS = (('1','1'),)
#
#
# class Building(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     building_type = models.CharField(max_length=100, CHOICES=BUILDING_TYPES, require=True)
#     building_age = models.FloatField(required=False, blank=True, null=True)
#     building_area = models.FloatField(required=False, blank=True, null=True)
#     key_place = models.CharField(max_length=256, required=False, blank=True, null=True)
#     building_category = models.CharField(max_length=100, CHOICES=BUILDING_CATEGORY, require=True)
#     building_usage = models.CharField(max_length=100, CHOICES=BUILDING_USAGE, require=True)
#     offer = models.CharField(max_length=100, CHOICES=OFFERS, require=True)
#     price = models.FloatField(required=False, blank=True, null=True)
#     soom_price = models.FloatField(required=False, blank=True, null=True)
#     payment_method = models.CharField(max_length=100, required=False, blank=True, null=True)
#     region = models.CharField(max_length=100, CHOICES=REGIONS, require=True)
#     city = models.CharField(max_length=100, CHOICES=CITIES, require=True)
#     neighborhood = models.CharField(max_length=100, CHOICES=NEIGHBORHOODS, require=True)
