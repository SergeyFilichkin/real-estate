from django.db import models # type: ignore

class Floor(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(db_index=True)

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этаж"
