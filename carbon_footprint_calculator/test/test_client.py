from django.test import TestCase


class SimpleTest(TestCase):
    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_1(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_heating_home_or_flat(self):
        response = self.client.get('/heating_home_or_flat/')
        self.assertEqual(response.status_code, 200)

    def test_travel(self):
        response = self.client.get('/heating_home_or_flat/')
        self.assertEqual(response.status_code, 200)

    def test_transport(self):
        response = self.client.get('/transport/')
        self.assertEqual(response.status_code, 200)

    def test_diet(self):
        response = self.client.get('/diet/')
        self.assertEqual(response.status_code, 200)

