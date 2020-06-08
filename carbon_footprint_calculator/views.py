from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from carbon_footprint_calculator.forms import *
from carbon_footprint_calculator.models import *


class MainView(View):
    def get(self, request):
        info = InformationPage.objects.all().filter(id=1)
        return render(request, "html/main.html", {"info": info})


class HouseView(View):
    def get(self, request):
        info = InformationPage.objects.all().filter(id=2)
        form = HouseForm()
        return render(request, "html/house.html", {"info": info, "form": form})

    def post(self, request):
        info = InformationPage.objects.all()
        form = HouseForm(request.POST)
        if form.is_valid():
            household = form.cleaned_data["household"]
            type_of_heating = form.cleaned_data["type_of_heating"]
            amount = form.cleaned_data["amount"]
            result = []
            if type_of_heating == "energia elektryczna [kWh]":
                formula = (int(amount) * 0.822)/int(household)
                result.append(round(formula, 2))
            elif type_of_heating == "gaz ziemny [kWh]":
                formula = (int(amount) * 0.195)/int(household)
                result.append(round(formula, 2))
            elif type_of_heating == "węgiel [t]":
                formula = (int(amount) * 0.0)/int(household)
                result.append(round(formula, 2))
            elif type_of_heating == "drewno opałowe [t]":
                formula = (int(amount) * 0.067)/int(household)
                result.append(round(formula, 2))
            elif type_of_heating == "LPG [l]":
                formula = (int(amount) * 3.03)/int(household)
                result.append(round(formula, 2))
            else:
                formula = (int(amount) * 2.92)/int(household)
                result.append(round(formula, 2))
            house = House.objects.create(household=household, type_of_heating=type_of_heating, amount=amount)
            return render(request, "html/result-house.html", {"house": house, "result": result})
        else:
            return render(request, "html/house.html", {"info": info, "form": form})


class TravelView(View):
    def get(self, request):
        info = InformationPage.objects.all().filter(id=3)
        form = TravelForm()
        return render(request, "html/travel.html", {"info": info, "form": form})

    def post(self, request):
        info = InformationPage.objects.all()
        form = TravelForm(request.POST)
        if form.is_valid():
            mode_of_transport = form.cleaned_data["mode_of_transport"]
            length_of_distance = form.cleaned_data["length_of_distance"]
            equivalent = form.cleaned_data["country"]
            number_of_night = form.cleaned_data["number_of_night"]
            result = []
            if mode_of_transport == "pociąg":
                formula = (int(length_of_distance)*0.015) + (int(number_of_night)*(float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "autokar":
                formula = (int(length_of_distance) * 0.03) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "somochód disel":
                formula = (int(length_of_distance) * 0.18) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "samochód hybrydowy":
                formula = (int(length_of_distance) * 0.12) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "samochód elektryczny":
                formula = (int(length_of_distance) * 0.06) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "lot krajowy":
                formula = (int(length_of_distance) * 0.123) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            elif mode_of_transport == "lot krótkodystansowy":
                formula = (int(length_of_distance) * 0.076) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            else:
                formula = (int(length_of_distance) * 0.094) + (int(number_of_night) * (float(equivalent)))
                result.append(round(formula, 2))
            travel = Travel.objects.create(mode_of_transport=mode_of_transport, length_of_distance=length_of_distance, number_of_night=number_of_night)
            return render(request, "html/result-travel.html", {"travel": travel, "result": result})
        else:
            return render(request, "html/house.html", {"info": info, "form": form})


class TransportView(View):
    def get(self, request):
        info = InformationPage.objects.all().filter(id=4)
        form = TransportForm()
        return render(request, "html/transport.html", {"info": info, "form": form})

    def post(self, request):
        info = InformationPage.objects.all()
        form = TransportForm(request.POST)
        if form.is_valid():
            form_of_moving = form.cleaned_data["form_of_moving"]
            distance_in_km = form.cleaned_data["distance_in_km"]
            result = []
            if form_of_moving == "rower":
                formula = (int(distance_in_km) * 0)
                result.append(round(formula, 2))
            if form_of_moving == "tramwaj":
                formula = (int(distance_in_km) * 0.06)
                result.append(round(formula, 2))
            elif form_of_moving == "metro":
                formula = (int(distance_in_km) * 0.059)
                result.append(round(formula, 2))
            elif form_of_moving == "autobus":
                formula = (int(distance_in_km) * 0.103)
                result.append(round(formula, 2))
            elif form_of_moving == "somochód disel":
                formula = (int(distance_in_km) * 0.18)
                result.append(round(formula, 2))
            elif form_of_moving == "samochód hybrydowy":
                formula = (int(distance_in_km) * 0.12)
                result.append(round(formula, 2))
            else:
                formula = (int(distance_in_km) * 0.06)
                result.append(round(formula, 2))
            transport = DailyTransport.objects.create(form_of_moving=form_of_moving, distance_in_km=distance_in_km)
            return render(request, "html/result-transport.html", {"transport": transport, "result": result})
        else:
            return render(request, "html/house.html", {"info": info, "form": form})


class DietView(View):
    def get(self, request):
        info = InformationPage.objects.all().filter(id=5)
        form = FoodForm()
        return render(request, "html/diet.html", {"info": info, "form": form})

    def post(self, request):
        info = InformationPage.objects.all()
        form = FoodForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data["product"]
            consumption = form.cleaned_data["consumption"]
            equivalent = form.cleaned_data["product"]
            result = round((int(consumption) * float(equivalent)), 2)
            return render(request, "html/result-diet.html", {"result": result})
        else:
            return render(request, "html/diet.html", {"info": info, "form": form})
