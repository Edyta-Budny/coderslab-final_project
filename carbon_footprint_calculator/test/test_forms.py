from django.core.exceptions import ValidationError
from django.test import TestCase

from carbon_footprint_calculator.forms import HouseForm
from carbon_footprint_calculator.models import House, Travel, DailyTransport, \
    Food


class TestHouseForm(TestCase):
    def test_create_obj(self):
        data = {
            "household": "1",
            "type_of_heating": "G",
            "amount": "-1",
        }
        form = HouseForm(data=data)
        self.assertFalse(form.is_valid())


class TestTravelForm(TestCase):
    def test_create_obj(self):
        data = {
            "mode_of_transport": "T",
            "length_of_distance": "400",
            "country": "53.8",
            "number_of_night": "6",
        }
        response = self.client.post("/travel/", data=data)
        self.assertEqual(Travel.objects.count(), 1)
        self.assertEqual(response.status_code, 200)


class TestTransportForm(TestCase):
    def test_create_obj(self):
        data = {
            "form_of_moving": "B",
            "distance_in_km": "20",
        }
        response = self.client.post("/transport/", data=data)
        self.assertEqual(DailyTransport.objects.count(), 1)
        self.assertEqual(response.status_code, 200)


class TestFoodForm(TestCase):
    def test_create_obj(self):
        data = {
            "name_food": "2.0",
            "equivalent": "300",
        }
        response = self.client.post("/diet/", data=data)
        self.assertEqual(Food.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
