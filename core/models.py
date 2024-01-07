from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.urls import reverse


class AppUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='app_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='app_users_permissions'
    )

    @property
    def full_name(self):
        first = self.first_name if self.first_name else ""
        last = self.last_name if self.last_name else ""
        return f'{first} {last}' if first and last else ""
    
class UserMixin(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)

    class Meta:
        abstract = True
# Create your models here.
class Student(models.Model):
    student = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    grade = models.ForeignKey('Grade',on_delete=models.CASCADE)
    institute = models.ForeignKey("Institute",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.student.first_name} {self.student.last_name}' 

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])
class Grade(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    


class Institute(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grade = models.ManyToManyField(Grade,blank=True)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name