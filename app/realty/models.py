from django.db import models

class Flat(models.Model):
    address = models.CharField(max_length=255)
    floor_area = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  #
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.address