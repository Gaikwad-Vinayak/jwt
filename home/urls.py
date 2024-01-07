from core.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from home.views import CourseViewSet

app_name = 'home'

router = DefaultRouter()
router.register(r'course', CourseViewSet,basename="course-detail")

urlpatterns = router.urls
