from django.db import models

NUMBER_OF_PEOPLE_IN_HOUSEHOLD = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

TYPE_OF_HEATING = (
    ("energia elektryczna [kWh]", "energia elektryczna [kWh]"),
    ("gaz ziemny [kWh]", "gaz ziemny [kWh]"),
    ("węgiel [t]", "węgiel [t]"),
    ("drewno opałowe [t]", "drewno opałowe [t]"),
    ("LPG [l]", "LPG [l]"),
    ("olej opałowy [l]", "olej opałowy [l]"),
)

MEANS_OF_TRANSPORT = (
    ("pociąg", "pociąg"),
    ("autokar", "autokar"),
    ("somochód disel", "somochód disel"),
    ("samochód hybrydowy", "samochód hybrydowy"),
    ("samochód elektryczny", "samochód elektryczny"),
    ("lot krajowy", "lot krajowy"),
    ("lot krótkodystansowy < 3700 km", "lot krótkodystansowy < 3700 km"),
    ("lot długodystansowy > 3700 km", "lot długodystansowy > 3700 km"),
)

DAILY_MEANS_OF_TRANSPORT = (
    ("rower", "rower"),
    ("tramwaj", "tramwaj"),
    ("metro", "metro"),
    ("autobus", "autobus"),
    ("somochód disel", "somochód disel"),
    ("samochód hybrydowy", "samochód hybrydowy"),
    ("samochód elektryczny", "samochód elektryczny"),
)


class InformationPage(models.Model):
    information = models.TextField()


class House(models.Model):
    household = models.IntegerField(
        choices=NUMBER_OF_PEOPLE_IN_HOUSEHOLD,
        verbose_name="Liczba osób w gospodarstwie domowym"
    )
    type_of_heating = models.CharField(
        max_length=120,
        choices=TYPE_OF_HEATING,
        verbose_name="Forma ogrzewania"
    )
    amount = models.IntegerField(
        verbose_name="Wartość zużyta"
    )


class Travel(models.Model):
    mode_of_transport = models.CharField(
        max_length=120,
        choices=MEANS_OF_TRANSPORT,
        verbose_name="Środek transportu"
    )
    length_of_distance = models.IntegerField(
        verbose_name="Pokonany dystans w km"
    )
    number_of_night = models.IntegerField(
        verbose_name="Liczba nocy"
    )


class Country(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="Kraj zakwaterowania"
    )
    equivalent = models.FloatField()

    @property
    def country(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.country


class DailyTransport(models.Model):
    form_of_moving = models.CharField(
        max_length=120,
        choices=DAILY_MEANS_OF_TRANSPORT,
        verbose_name="Środek transportu"
    )
    distance_in_km = models.IntegerField(
        verbose_name="Pokonany dystans w km"
    )


class Food(models.Model):
    name_food = models.CharField(
        max_length=120
    )
    equivalent = models.FloatField()

    @property
    def food(self):
        return "{}".format(self.name_food)

    def __str__(self):
        return self.food
