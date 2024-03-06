from django.core.validators import MinValueValidator
from django.db import models


class Flat(models.Model):
    square = models.FloatField(verbose_name='Общая площадь', validators=[MinValueValidator(limit_value=0)])
    living_space = models.FloatField(verbose_name='Жилая площадь', validators=[MinValueValidator(limit_value=0)])
    kitchen_area = models.FloatField(verbose_name='Площадь кухни', validators=[MinValueValidator(limit_value=0)])
    rooms = models.PositiveSmallIntegerField(verbose_name='Количество комнат')
    floor = models.PositiveSmallIntegerField(verbose_name='Этаж')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField()
