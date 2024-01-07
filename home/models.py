from django.db import models

# Create your models here.

class CourseMaster(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    number_of_student = models.IntegerField(default=1)
    