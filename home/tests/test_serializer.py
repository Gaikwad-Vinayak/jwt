from rest_framework.test import APITestCase, APIClient
from home.serializers import CourseSerializer
from home.models import CourseMaster

class TestSerializer(APITestCase):
    def setUp(self):
        self.data = {
            "name":"Math",
            "number_of_student":5,
        }
        self.update_data = {
            "id":1,
            "name":"updated data",
            "number_of_student":100
        }

    def test_get_serializer(self):
        instance = CourseSerializer(data=self.data)
        self.assertTrue(instance.is_valid())
        validate_data  = instance.validated_data
        self.assertEqual(validate_data['name'],"Math")

    def test_create_serializer(self):
        instance = CourseSerializer(data=self.data)
        self.assertTrue(instance.is_valid())
        self.assertEqual(instance.errors,{})

    def test_update_serializer(self):
        # model_instance = CourseMaster.objects.create(**self.data)
        instance = CourseSerializer(data=self.update_data)
        self.assertTrue(instance.is_valid())
        validate_data = instance.validated_data
        self.assertEqual(validate_data['name'],"updated data")
        self.assertEqual(instance.errors,{})

