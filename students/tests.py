import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")  # Cambiá por tu proyecto real
django.setup()

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class StudentAPITestCase(APITestCase):

    def setUp(self):
        self.student_data = {
            "first_name": "Scarlett",
            "last_name": "Evans",
            "date_of_birth": "2010-05-01",
            "grade": 8,
            "phone": "+111111111111",
            "email": "scarlet@email.com"
        }
        self.create_url = reverse('student-list')  # nombre de la ruta en tu router

    def test_create_student(self):
        response = self.client.post(self.create_url, self.student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "Scarlett")