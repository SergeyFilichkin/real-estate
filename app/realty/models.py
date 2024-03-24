from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    overall_square = models.IntegerField()
    living_square = models.IntegerField()
    rooms = models.IntegerField()
    view_from_windows = models.CharField(max_length=120)
    lavatory = models.IntegerField()
    level = models.IntegerField()
    elevator = models.CharField(max_length=120)
    year_of_sale = models.IntegerField()
    parking = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=True)
    is_kitchen = models.BooleanField()
