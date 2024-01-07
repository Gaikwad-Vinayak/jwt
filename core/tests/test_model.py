from django.test import TestCase
from core.models import AppUser

class TestCaseUser(TestCase):
    def test_create_user(self):
        first_name = "vinayak"
        last_name = "gaikwad"
        email = "gaikwadvinayak@gmail.com"
        gender = "Male"
        phone = "9988778897"
        password = "12345"
    
        user = AppUser.objects.create(first_name=first_name,last_name=last_name,
                                    email=email,gender=gender, phone=phone,password=password,
                                    username=phone)
        
        user.set_password(password)
        user.save()
        self.assertEqual(user.first_name,first_name)
        self.assertEqual(user.last_name,last_name)
        self.assertEqual(user.phone,phone)
        self.assertEqual(user.email,email)
        self.assertEqual(user.gender,gender)
        self.assertTrue(user.check_password(password))

class TestCaseUserPar(TestCase):
    def test_get_full_name(self):
        first_name = "vinayak"
        last_name = "gaikwad"
        user = AppUser(first_name=first_name,last_name=last_name)
        self.assertEqual(user.full_name,"vinayak gaikwad")
        print(f"first_name: {user.first_name}")
        print(f"last_name: {user.last_name}")

