from django.db import models
from django.core.validators import MinValueValidator

from .building import Building
from .flatcategory import FlatCategory
from .floor import Floor


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
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT, verbose_name="Этаж")
    category = models.ForeignKey(FlatCategory, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Класс квартиры')
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.PROTECT)
