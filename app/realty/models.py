from django.db import models


class Floor(models.Model):
    number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Этаж"
        Verbose_name_plural = "Этажи"

    def __str__(self):
        return self.number


class Flat(models.Model):
    COURTYARD = "courtyard"
    STREET_OUTSIDE = "street_outside"
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
    price = models.PositiveIntegerField()
    overall_square = models.PositiveIntegerField()
    living_square = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    view_from_windows = models.CharField(max_length=120, choices=WINDOW_VIEWS, default=COURTYARD, blank=True)
    lavatory = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    elevator = models.PositiveIntegerField()
    year_of_sale = models.PositiveIntegerField()
    parking = models.CharField(max_length=50, choices=PARKING_CHOICES, default=ON_GROUND)
    is_complete = models.BooleanField(default=False)
    has_kitchen = models.BooleanField()
    floor = models.ManyToManyField(Floor)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return self.name
