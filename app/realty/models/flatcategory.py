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

    def __str__(self) -> str:
        """returns FlateCategory neme description"""
        return self.get_name_display()
