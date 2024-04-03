from django.db import models

from .project import Project


class Building(models.Model):
    STATUS_UNDER_CONSTRUCTION = 'Under construction'
    STATUS_PASSED = 'Passed'

    STATUS_CHOICES = [
        (STATUS_UNDER_CONSTRUCTION, 'Строится'),
        (STATUS_PASSED, 'Сдан')
    ]

    TYPE_BUILDING_CHOICES = [
        ('Brick', 'Кирпичный'),
        ('Monolithic', 'Монолитный'),
        ('Panel', 'Панельный'),
    ]

    ZERO_ELEVATORS = 0
    ONE_ELEVATOR = 1
    TWO_ELEVATORS = 2
    THREE_ELEVATORS = 3

    ELEVATORS_CHOICES = [
        (ZERO_ELEVATORS, 'Ноль'),
        (ONE_ELEVATOR, 'Один'),
        (TWO_ELEVATORS, 'Два'),
        (THREE_ELEVATORS, 'Три')
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    floors = models.PositiveSmallIntegerField(verbose_name='Количество этажей')
    date_of_construction = models.DateField(verbose_name='Дата постройки дома')
    date_of_delivery = models.DateField(verbose_name='Дата сдачи дома')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    number = models.PositiveSmallIntegerField(verbose_name='Номер дома', db_index=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_UNDER_CONSTRUCTION, verbose_name='Статус')
    type = models.CharField(max_length=10, choices=TYPE_BUILDING_CHOICES, null=True, blank=True, verbose_name='Тип дома')
    has_parking = models.BooleanField(default=True, verbose_name='Паркинг')
    elevators = models.IntegerField(choices=ELEVATORS_CHOICES, default=TWO_ELEVATORS, verbose_name='Лифты')
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.PROTECT)
