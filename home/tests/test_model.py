from django.test import TestCase
from home.models import CourseMaster


class CourseTestView(TestCase):
    def setUp(self):
        self.data = {
            "name":"new course",
            "start_date":"2001-01-27",
            "start_date":"2001-01-27",
            "number_of_student":5,
            "subject":"math"
        }
        self.update_data = {
                    "id":1,
                    "name":"update course",
                    "start_date":"2001-01-27",
                    "start_date":"2001-01-27",
                    "number_of_student":5,
                    "subject":"math"
                }
    
    def test_get_course(self):
        instance = CourseMaster.objects.create(**self.data)
        created_instance = CourseMaster.objects.get(id=instance.id)
        self.assertTrue(instance,created_instance)
    
    def test_create_course(self):
        instance = CourseMaster.objects.create(**self.data)
        instance.save()
        self.assertEqual(instance.name,"new course")

    def test_update_course(self):
        instance = CourseMaster.objects.create(**self.data)
        instance.save()
        instance.__dict__.update(**self.update_data)
        instance.save()
        self.assertEqual(instance.name,"update course")

    def test_delete_course(self):
        instance = CourseMaster.objects.create(**self.data)
        instance.save()
        instance.delete()
        try:
            deleted_instance = CourseMaster.objects.get(id=instance.id)
        except:
            deleted_instance =  None
        self.assertEqual(deleted_instance,None)