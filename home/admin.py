from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CourseMaster)
class admincourse(admin.ModelAdmin):
    list_display = ['name']