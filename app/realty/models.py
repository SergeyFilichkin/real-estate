<<<<<<< HEAD
from django.db import models


class Flat(models.Model):
    COURTYARD = "courtyard"
    STREET_OUTSIDE = "street_outside"
    WINDOW_VIEWS = [
        (COURTYARD, "внутренний двор"),
        (STREET_OUTSIDE, "внешняя улица")
    ]
    ON_GROUND = "on_ground"
    UNDERGROUND = "underground"

    PARKING_CHOICES = (
        (ON_GROUND, "наземный"),
        (UNDERGROUND, "подземный")
    )

    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    overall_square = models.IntegerField()
    living_square = models.IntegerField()
    rooms = models.IntegerField()
    view_from_windows = models.CharField(max_length=120, choices=WINDOW_VIEWS, default=COURTYARD, blank=True)
    lavatory = models.IntegerField()
    level = models.IntegerField()
    elevator = models.CharField(max_length=120)
    year_of_sale = models.IntegerField()
    parking = models.CharField(max_length=50, choices=PARKING_CHOICES, default=ON_GROUND)
    is_complete = models.BooleanField(default=True)
    is_kitchen = models.BooleanField()
=======
from django.db import models


class Flat(models.Model):
    WINDOW_VIEWS = [
        ("courtyard", "внутренний двор"),
        ("street_outside", "внешняя улица")
    ]
    ON_GROUND = "on_ground"
    UNDERGROUND = "underground"

    PARKING_CHOICES = (
        (ON_GROUND, "наземный"),
        (UNDERGROUND, "подземный")
    )

    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    overall_square = models.IntegerField()
    living_square = models.IntegerField()
    rooms = models.IntegerField()
    view_from_windows = models.CharField(max_length=120, choices=WINDOW_VIEWS, default="courtyard", blank=True)
    lavatory = models.IntegerField()
    level = models.IntegerField()
    elevator = models.CharField(max_length=120)
    year_of_sale = models.IntegerField()
    parking = models.CharField(max_length=50, choices=PARKING_CHOICES, default=ON_GROUND)
    is_complete = models.BooleanField(default=True)
    is_kitchen = models.BooleanField()
>>>>>>> fa9e7f8 (M-4: Внесение изменений в .gitignore)
