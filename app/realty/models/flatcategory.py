from django.db import models


class FlatCategory(models.Model):
    ECONOMY = 'Economy'
    COMFORT = 'Comfort'
    LUXE = 'Luxe'

    CLASS_CHOICES = [
        (ECONOMY, 'Эконом'),
        (COMFORT, 'Комфорт'),
        (LUXE, 'Люкс')
    ]

    name = models.CharField(max_length=7, choices=CLASS_CHOICES, db_index=True)
