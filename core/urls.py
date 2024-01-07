from core.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.fcm_views import FCMNotificationView

app_name = 'core'

router = DefaultRouter()
router.register(r'student', StudentViewSet,basename="student_crud")
router.register(r'grade', GradeViewSet,basename="grade")
router.register(r'institute', InstituteViewSet,basename="institute")
urlpatterns = router.urls

# urlpatterns.append(path('v1/seminars', SeminarViewSet.as_view()))
urlpatterns.append(path('send-notification/', FCMNotificationView.as_view(), name='send-notification')),

