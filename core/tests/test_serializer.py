from django.test import TestCase
from core.models import AppUser
from core.serializers import *
from rest_framework.test import APITestCase

class UserSerializerTestCase(APITestCase):
    def test_user_serializer(self):
        data = {
            "username":"8390987654",
            "first_name":"vinayak",
            "last_name":"gaikwad"
        }
        seri = AppuserSerializers(data=data)
        self.assertTrue(seri.is_valid())
        self.assertEqual(seri.errors,{})