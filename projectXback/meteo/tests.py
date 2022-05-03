from django.test import TestCase
from .models import Stations

class ViewsTestCase(TestCase):
    def test_api_stations_load_properly(self):
        response = self.client.get('http://127.0.0.1:8000/api/stations')
        self.assertEqual(response.status_code, 200)

class ModelsTestCase(TestCase):
    def test_insert_to_DB(self):
        Stations.objects.create(ids='test_id', name='test_name', country='Russia', coordinateX='0.0', coordinateY='0.0', validFrom='1970-01-01')

