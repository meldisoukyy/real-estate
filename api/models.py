from django.utils.translation import gettext_lazy as _
from django.db import models
from accounts.models import User


# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الالكتروني")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    message = models.TextField(verbose_name="الرسالة")

    class Meta:
        verbose_name = _("طلبات التواصل")
        verbose_name_plural = _("طلبات التواصل")

    def __str__(self):
        return self.name


class JoinUsForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.TextField()

    class Meta:
        verbose_name = _("طلبات الانضمام")
        verbose_name_plural = _("طلبات الانضمام")

    def __str__(self):
        return self.name


# BUILDING_USAGE = (('1','1'),)
# OFFERS = (('1', '1'),)
# PAYMENT_METHODS = (('1', '1'),)
# REGIONS = (('1', '1'),)
# CITIES = (('1', '1'),)
# NEIGHBORHOODS = (('1', '1'),)
#

class Building(models.Model):
    class BuildingTypes(models.TextChoices):
        WORKERS_HOUSE = '1', 'Workers_houses'
        GALLERIES = '2', 'Galleries'
        FARM = '3', 'Farm'

    class BuildingCategory(models.TextChoices):
        HOUSING = '1', 'Housing'
        COMMERCIAL = '2', 'Commercial'
        AGRICULTURAL = '3', 'Agricultural'
        INDUSTRIAL = '4', 'Industrial'

    class BuildingUsage(models.TextChoices):
        SINGLES = '1', 'Singles'
        FAMILIES = '2', 'Families'
        OFFICE = '3', 'Office'

    class Offer(models.TextChoices):
        RENT = '1', 'Singles'
        SALE = '2', 'Families'
        AUCTION = '3', 'Auction'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building_type = models.CharField(max_length=100, choices=BuildingTypes.choices, blank=False)
    building_age = models.FloatField(blank=True, null=True)
    building_area = models.FloatField(blank=True, null=True)
    key_place = models.CharField(max_length=256, blank=True, null=True)
    building_category = models.CharField(max_length=100, choices=BuildingCategory.choices, blank=False)
    building_usage = models.CharField(max_length=100, choices=BuildingUsage.choices, blank=False)
    offer = models.CharField(max_length=100, choices=Offer.choices, blank=False)
    price = models.FloatField(blank=True, null=True)
    soom_price = models.FloatField(blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.building_category

    class Meta:
        verbose_name = _("العقارات")
        verbose_name_plural = _("العقارات")


class BuildingLocation(models.Model):
    class Region(models.TextChoices):
        EAST_REGION = '1', 'المنطقة الشرقية'
        HAEL = '2', 'حائل'
        REYAD = '3', 'الرياض'
        DMAM = '4', 'الدمام'
        QUSIEM = '5', 'القصيم'

    class City(models.TextChoices):
        HAEL = '2', 'حائل'
        REYAD = '3', 'الرياض'
        DMAM = '4', 'الدمام'
        QUSIEM = '5', 'القصيم'

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    region = models.CharField(max_length=100, choices=Region.choices, blank=False)
    # city = models.CharField(max_length=100, CHOICES=CITIES, require=True)
    # neighborhood = models.CharField(max_length=100, CHOICES=NEIGHBORHOODS, require=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = _("موقع العقار")
        verbose_name_plural = _("موقع العقار")

    def __str__(self):
        return self.building.building_category
