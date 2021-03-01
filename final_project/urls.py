from django.contrib import admin
from django.urls import path

from carbon_footprint_calculator.views import *

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('main/', MainView.as_view(), name="main"),
    path('heating_home_or_flat/', HouseView.as_view(), name="home"),
    path('travel/', TravelView.as_view(), name="travel"),
    path('transport/', TransportView.as_view(),  name="transport"),
    path('diet/', DietView.as_view(), name="diet"),
    path('admin/', admin.site.urls),
]
