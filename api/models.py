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

    class Region(models.TextChoices):
        EAST_REGION = '1', 'المنطقة الشرقية'
        HAEL = '2', 'حائل'
        REYAD = '3', 'الرياض'
        DMAM = '4', 'الدمام'
        QUSIEM = '5', 'القصيم'

    class City(models.TextChoices):
        HAFR_AL_BATIN = '1', 'حفر الباطن'
        HAEL = '2', 'حائل'
        REYAD = '3', 'الرياض'
        DMAM = '4', 'الدمام'
        BAREDA = '5', 'بريدة'

    class Neighborhood(models.TextChoices):
        ALMOHAMMADIAH = '1', 'المحمدية'
        ALKAHFYA = '2', 'الكهيفية'
        RAYAN = '3', 'الريان'
        NAHDA = '4', 'النهضة'
        BAREDA = '5', 'بريدة'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building_type = models.CharField(max_length=100,blank=False)
    building_age = models.FloatField(blank=True, null=True)
    building_area = models.FloatField(blank=True, null=True)
    key_place = models.CharField(max_length=256, blank=True, null=True)
    building_category = models.CharField(max_length=100, blank=False)
    building_usage = models.CharField(max_length=100, blank=False)
    offer = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=True, null=True)
    soom_price = models.FloatField(blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True)
    apartments = models.IntegerField(blank=True, null=True)
    ground_floor_rooms = models.IntegerField(blank=True, null=True)
    upper_floor_rooms = models.IntegerField(blank=True, null=True)
    split_air_conditioner = models.IntegerField(blank=True, null=True)
    window_air_conditioner = models.IntegerField(blank=True, null=True)
    hall = models.IntegerField(blank=True, null=True)
    parking = models.IntegerField(blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    driver_room = models.IntegerField(blank=True, null=True)
    elevators = models.IntegerField(blank=True, null=True)
    kitchen = models.BooleanField(default=False)
    seperated_entrance = models.BooleanField(default=False)
    warehouse = models.BooleanField(default=False)
    car_entrance = models.BooleanField(default=False)
    shared_entrance = models.BooleanField(default=False)
    seperated_2_floors = models.BooleanField(default=False)
    Central_air_conditioning = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    rooftop = models.CharField(max_length=256, blank=True, null=True)
    mez_hall = models.BooleanField(default=False)  # صالة ميزانين
    well = models.BooleanField(default=False)
    pieces = models.IntegerField(blank=True, null=True)
    piece_number = models.IntegerField(blank=True, null=True)
    design_number = models.IntegerField(blank=True, null=True)  # رقم المخطط
    region = models.CharField(max_length=100,  blank=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100,  blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.building_category

    class Meta:
        verbose_name = _("العقارات")
        verbose_name_plural = _("العقارات")


class BuildingImage(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='building_images/')

# class Rate Building
