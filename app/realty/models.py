from django.core.validators import MinValueValidator
from django.db import models


class Flat(models.Model):

    STATUS_CHOICES = [
        ('On sale', 'В продаже'),
        ('Sold', 'Продана')
    ]

    square = models.FloatField(verbose_name='Общая площадь', validators=[MinValueValidator(limit_value=0)])
    living_space = models.FloatField(verbose_name='Жилая площадь', validators=[MinValueValidator(limit_value=0)])
    kitchen_area = models.FloatField(verbose_name='Площадь кухни', validators=[MinValueValidator(limit_value=0)])
    rooms = models.PositiveSmallIntegerField(verbose_name='Количество комнат')
    floor = models.PositiveSmallIntegerField(verbose_name='Этаж')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='On sale', verbose_name='Статус')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField()
