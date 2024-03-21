from django.db import models



class Flat(models.Model):
    residential_address = models.CharField(max_length=255)
    floor_area = models.IntegerField()
    apartment_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.residential_address




