from django.core.validators import MinValueValidator
from django.db import models


class Flat(models.Model):

    STATUS_CHOICES = [("On sale", "В продаже"), ("Sold", "Продана")]

    square = models.FloatField(
        verbose_name="Общая площадь", validators=[MinValueValidator(limit_value=0)]
    )
    living_space = models.FloatField(
        verbose_name="Жилая площадь", validators=[MinValueValidator(limit_value=0)]
    )
    kitchen_area = models.FloatField(
        verbose_name="Площадь кухни", validators=[MinValueValidator(limit_value=0)]
    )
    rooms = models.PositiveSmallIntegerField(verbose_name="Количество комнат")
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default="On sale", verbose_name="Статус"
    )
    price = models.PositiveBigIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    floor = models.ForeignKey("Floor", on_delete=models.PROTECT, verbose_name="Этаж")
    category = models.ForeignKey('FlatCategory', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Класс квартиры')
    building = models.ForeignKey('Building', null=True, blank=True, on_delete=models.PROTECT)


class Floor(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(db_index=True)


class FlatCategory(models.Model):
    CLASS_CHOICES = [
        ('Economy', 'Эконом'),
        ('Comfort', 'Комфорт'),
        ('Luxe', 'Люкс')
    ]

    name = models.CharField(max_length=7, choices=CLASS_CHOICES, db_index=True)


class Building(models.Model):
    STATUS_CHOICES = [
        ('Under construction', 'Строится'),
        ('Passed', 'Сдан')
    ]

    TYPE_BUILDING_CHOICES = [
        ('Brick', 'Кирпичный'),
        ('Monolithic', 'Монолитный'),
        ('Panel', 'Панельный'),

    ]

    PARKING_CHOICES = [
        ('Present', 'Присутствует'),
        ('Missing', 'Отсутствует')
    ]

    ELEVATORS_CHOICES = [
        ('Missing', 'Отсутсвуют'),
        ('One', 'Один'),
        ('Two', 'Два'),
        ('Three', 'Три')
    ]

    name = models.CharField(max_length=100)
    date_of_construction = models.DateField()
    address = models.CharField(max_length=100, verbose_name='Адрес')
    number = models.PositiveSmallIntegerField(verbose_name='Номер дома', db_index=True)
    status = models.CharField(max_length=18, choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Статус')
    type = models.CharField(max_length=10, choices=TYPE_BUILDING_CHOICES, null=True, blank=True, verbose_name='Тип дома')
    parking = models.CharField(max_length=7, choices=PARKING_CHOICES, null=True, blank=True, verbose_name='Паркинг')
    elevators = models.CharField(max_length=7, choices=ELEVATORS_CHOICES, null=True, blank=True, verbose_name='Лифты')
