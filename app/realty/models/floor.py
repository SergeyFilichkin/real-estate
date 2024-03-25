from django.db import models


class Floor(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(db_index=True)
