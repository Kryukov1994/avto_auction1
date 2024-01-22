from django.db import models
from django.contrib.auth.models import User


class Avto(models.Model):
    
    BRAND_CHOICES = (
        ('audi', 'Ауди'),
        ('bmw', 'БМВ'),
        ('honda', 'Хонда'),
        ('mazda', 'Мазда'),
        ('mercedes', 'Мерседес'),
        ('nissan', 'Ниссан'),
        ('toyota', 'Тойота'),
    )
    
    STEERING_CHOICES = (
        ('left', 'Левосторонний'),
        ('right', 'Правосторонний'),
    )

    TRANSMISSION_CHOICES = (
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('robot', 'Робот'),
    )
    
    DRIVE_CHOICES = (
        ('front', 'Передний'),
        ('rear', 'Задний'),
        ('4wd', '4 WD'),
    )
    
    FUEL_CHOICES = (
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('gas', 'Газ'),
        ('electric', 'Электро'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    city = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    steering = models.CharField(max_length=10, choices=STEERING_CHOICES)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)  # поле с виджетом КПП
    drive = models.CharField(max_length=10, choices=DRIVE_CHOICES)  # поле с виджетом привод
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICES)  # поле с виджетом топливо
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='avtoimg/%Y/%m/%d', blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self. brand