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


class ContractRequestForm(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    contract_duration = models.CharField(max_length=100, verbose_name="مدة العقد")
    contract_type = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="نوع العقد"
    )
    region = models.CharField(max_length=100, blank=False)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("العقد الالكتروني")
        verbose_name_plural = _("العقود الالكترونية")

    def __str__(self):
        return self.name


class Building(models.Model):
    class RequestState(models.TextChoices):
        PENDING = "1", "معلق"
        APPROVED = "2", "تمت الموافقة عليه"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building_type = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='نوع العقار'
    )
    building_age = models.FloatField(blank=True, null=True)
    building_area = models.FloatField(blank=True, null=True)
    building_number = models.CharField(max_length=100, blank=True, null=True)
    building_notes = models.TextField(blank=True, null=True)
    key_place = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    building_category = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='تصنيف العقار'
    )
    building_usage = models.CharField(max_length=100, blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)
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
    driver_room = models.BooleanField(blank=True, null=True)
    elevators = models.IntegerField(blank=True, null=True)
    kitchen = models.BooleanField(default=False, blank=True, null=True)
    seperated_entrance = models.BooleanField(default=False, blank=True, null=True)
    warehouse = models.BooleanField(default=False, blank=True, null=True)
    car_entrance = models.BooleanField(default=False, blank=True, null=True)
    shared_entrance = models.BooleanField(default=False, blank=True, null=True)
    seperated_2_floors = models.BooleanField(default=False, blank=True, null=True)
    Central_air_conditioning = models.BooleanField(default=False, blank=True, null=True)
    gas = models.BooleanField(default=False, blank=True, null=True)
    sauna = models.BooleanField(default=False, blank=True, null=True)
    pool = models.BooleanField(default=False, blank=True, null=True)
    electricity = models.BooleanField(default=False, blank=True, null=True)
    rooftop = models.CharField(max_length=256, blank=True, null=True)
    mez_hall = models.BooleanField(default=False, blank=True, null=True)  # صالة ميزانين
    well = models.BooleanField(default=False, blank=True, null=True)  # بئر
    pieces = models.IntegerField(blank=True, null=True)
    piece_number = models.IntegerField(blank=True, null=True)
    design_number = models.IntegerField(blank=True, null=True)  # رقم المخطط
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    state = models.CharField(
        max_length=1,
        choices=RequestState.choices,
        default=RequestState.PENDING,
        verbose_name="حالة الطلب",
        blank=True,
        null=True,
    )
    units_number = models.IntegerField(blank=True, null=True)
    plan_number = models.IntegerField(blank=True, null=True)
    pieces_number = models.IntegerField(blank=True, null=True)
    shops = models.IntegerField(blank=True, null=True)
    electricity_meter = models.IntegerField(blank=True, null=True)
    water_meter = models.IntegerField(blank=True, null=True)
    roof = models.CharField(max_length=100, blank=True, null=True)
    servant_room = models.BooleanField(default=False, blank=True, null=True)
    steam_bath = models.BooleanField(default=False, blank=True, null=True)
    furnished = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.building_category

    class Meta:
        verbose_name = _("العقارات")
        verbose_name_plural = _("العقارات")


class BuildingImage(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='building_images/')

    def __str__(self):
        return self.building.building_category

    class Meta:
        verbose_name = _("صور العقار")
        verbose_name_plural = _("صور العقار")


# class Rate Building
