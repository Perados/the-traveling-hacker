import requests

from rest_framework import status
from django.test import LiveServerTestCase

class ReadUserTest(LiveServerTestCase):
    def setUp(self):
        self.handle = 'justinbieber'

    def test_can_read_user_detail(self):
        response = requests.get("http://localhost:8082/api/twitter-users/" + self.handle)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReadUserErrorTest(LiveServerTestCase):
   def setUp(self):
       self.handle = 'justin bieber'

   def test_can_detect_non_existent_user(self):
       response = requests.get("http://localhost:8082/api/twitter-users/" + self.handle)
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       self.assertTrue(response.json()['error'])

