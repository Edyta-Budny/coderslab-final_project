from django import forms
from carbon_footprint_calculator.models import *
from django.core.exceptions import ValidationError


def AmountValidator(value):
    if not value >= 1:
        raise ValidationError(f"Wartość musi być większa od 0")


class HouseForm(forms.Form):
    household = forms.ChoiceField(label="Liczba osób w gospodarstwie domowym", choices=NUMBER_OF_PEOPLE_IN_HOUSEHOLD)
    type_of_heating = forms.ChoiceField(label="Forma ogrzewania", choices=TYPE_OF_HEATING)
    amount = forms.IntegerField(label="Wartość zurzyta", validators=[AmountValidator])


class TravelForm(forms.Form):
    mode_of_transport = forms.ChoiceField(label="Środek transportu", choices=MEANS_OF_TRANSPORT)
    length_of_distance = forms.IntegerField(label="Pokonany dystans w km", validators=[AmountValidator])
    countries = Country.objects.all().order_by("name")
    countries_choices = [(country.equivalent, country.name) for country in countries]
    country = forms.ChoiceField(label="Kraj zakwaterowania", choices=countries_choices)
    number_of_night = forms.IntegerField(label="Liczba nocy", validators=[AmountValidator])


class TransportForm(forms.Form):
    form_of_moving = forms.ChoiceField(choices=DAILY_MEANS_OF_TRANSPORT, label="Środek transportu")
    distance_in_km = forms.IntegerField(label="Pokonany dystans w km", validators=[AmountValidator])


class FoodForm(forms.Form):
    products = Food.objects.all().order_by("name_food")
    products_choices = [(product.equivalent, product.name_food) for product in products]
    product = forms.ChoiceField(label="Nazwa produktu", choices=products_choices)
    consumption = forms.IntegerField(label="Spożycie w kaloriach", validators=[AmountValidator])
