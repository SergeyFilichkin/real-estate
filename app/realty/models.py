from django.core.validators import MinValueValidator
from django.db import models


class Flat(models.Model):
    ON_SALE = 'On sale'
    SOLD = 'Sold'

    STATUS_CHOICES = [(ON_SALE, "В продаже"), (SOLD, "Продана")]

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
        max_length=7, choices=STATUS_CHOICES, default=ON_SALE, verbose_name="Статус"
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
    STATUS_UNDER_CONSTRUCTION = 'Under construction'
    STATUS_PASSED = 'Passed'

    STATUS_CHOICES = [
        (STATUS_UNDER_CONSTRUCTION, 'Строится'),
        (STATUS_PASSED, 'Сдан')
    ]

    TYPE_BUILDING_CHOICES = [
        ('Brick', 'Кирпичный'),
        ('Monolithic', 'Монолитный'),
        ('Panel', 'Панельный'),
    ]

    ZERO_ELEVATORS = 0
    ONE_ELEVATOR = 1
    TWO_ELEVATORS = 2
    THREE_ELEVATORS = 3

    ELEVATORS_CHOICES = [
        (ZERO_ELEVATORS, 'Ноль'),
        (ONE_ELEVATOR, 'Один'),
        (TWO_ELEVATORS, 'Два'),
        (THREE_ELEVATORS, 'Три')
    ]

    name = models.CharField(max_length=100)
    date_of_construction = models.DateField(verbose_name='Дата постройки дома')
    date_of_delivery = models.DateField(verbose_name='Дата сдачи дома')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    number = models.PositiveSmallIntegerField(verbose_name='Номер дома', db_index=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_UNDER_CONSTRUCTION, verbose_name='Статус')
    type = models.CharField(max_length=10, choices=TYPE_BUILDING_CHOICES, null=True, blank=True, verbose_name='Тип дома')
    has_parking = models.BooleanField(default=True, verbose_name='Паркинг')
    elevators = models.IntegerField(choices=ELEVATORS_CHOICES, default=TWO_ELEVATORS, verbose_name='Лифты')
