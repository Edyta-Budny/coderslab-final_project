from django.db import models


class InformationPage(models.Model):
    information = models.TextField()


class Household(models.Model):
    size = models.IntegerField(
        verbose_name="Liczba osób w gospodarstwie domowym",
    )


class Heating(models.Model):
    type = models.CharField(
        max_length=120,
        verbose_name="Forma ogrzewania"
    )
    usage = models.IntegerField(
        verbose_name="Wartość zużyta",
        null=True
    )
    equivalent = models.FloatField()


class Travel(models.Model):
    mode_of_transport = models.CharField(
        max_length=120,
        verbose_name="Środek transportu"
    )
    distance = models.IntegerField(
        verbose_name="Pokonany dystans w km",
        null=True
    )
    nights = models.IntegerField(
        verbose_name="Liczba nocy",
        null=True
    )
    equivalent = models.FloatField()


class Country(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="Kraj zakwaterowania"
    )
    equivalent = models.FloatField()


class DailyTransport(models.Model):
    type = models.CharField(
        max_length=120,
        verbose_name="Środek transportu"
    )
    distance = models.IntegerField(
        verbose_name="Pokonany dystans w km",
        null=True
    )
    equivalent = models.FloatField()


class Product(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name="Nazwa produktu",
    )
    consumption = models.FloatField(
        verbose_name="Spożycie w kaloriach",
        null=True
    )
    equivalent = models.FloatField()
