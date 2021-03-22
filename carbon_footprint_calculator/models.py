from django.db import models

from carbon_footprint_calculator.data.extractor import GetAccommodationData

NUMBER_OF_PEOPLE_IN_HOUSEHOLD = [(x, str(x)) for x in range(1, 11)]


class InformationPage(models.Model):
    information = models.TextField()


class House(models.Model):
    ELECTRICITY = "E"
    GAS = "G"
    CARBON = "C"
    FIREWOOD = "W"
    LPG = "L"
    FUEL_OIL = "O"
    TYPE_OF_HEATING = [
        (ELECTRICITY, "energia elektryczna [kWh]"),
        (GAS, "gaz ziemny [kWh]"),
        (CARBON, "węgiel [t]"),
        (FIREWOOD, "drewno opałowe [t]"),
        (LPG, "LPG [l]"),
        (FUEL_OIL, "olej opałowy [l]"),
    ]
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
    TRAIN = "T"
    BUS = "B"
    DISEL_CAR = "DE"
    HYBRID_CAR = "HE"
    ELECTRIC_CAR = "EC"
    DOMESTIC_FLIGHT = "DF"
    SHORT_HAUL_FLIGHT = "SF"
    LONG_HAUL_FLIGHT = "LF"
    MEANS_OF_TRANSPORT = [
        (TRAIN, "pociąg"),
        (BUS, "autokar"),
        (DISEL_CAR, "somochód disel"),
        (HYBRID_CAR, "samochód hybrydowy"),
        (ELECTRIC_CAR, "samochód elektryczny"),
        (DOMESTIC_FLIGHT, "lot krajowy"),
        (SHORT_HAUL_FLIGHT, "lot krótkodystansowy < 3700 km"),
        (LONG_HAUL_FLIGHT, "lot długodystansowy > 3700 km"),
    ]
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
        choices=GetAccommodationData(),
        verbose_name="Kraj zakwaterowania"
    )
    equivalent = models.FloatField()

    @property
    def country(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.country


class DailyTransport(models.Model):
    BIKE = "B"
    TRAM = "T"
    METRO = "M"
    BUS = "B"
    DISEL_CAR = "DE"
    HYBRID_CAR = "HE"
    ELECTRIC_CAR = "EC"
    DAILY_MEANS_OF_TRANSPORT = [
        (BIKE, "rower"),
        (TRAM, "tramwaj"),
        (METRO, "metro"),
        (BUS, "autobus"),
        (DISEL_CAR, "somochód disel"),
        (HYBRID_CAR, "samochód hybrydowy"),
        (ELECTRIC_CAR, "samochód elektryczny"),
    ]
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
