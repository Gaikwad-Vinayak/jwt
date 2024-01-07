from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestViewSet(APITestCase):
    def setUp(self):
        # print(reverse('course'),'88888888888888888888888') 
        self.url = "http://127.0.0.1:8000/home/course/"

        print(self.url,'999999999999')
        self.data = {
            "name":"vinayak",
            "number_of_student":5
        }


    def test_create_data(self):
        response = self.client.post(self.url, self.data, format='json')
        print(response,'5555555555555')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
