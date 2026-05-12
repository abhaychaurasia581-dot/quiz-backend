
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet
from .views import student_list


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('', include(router.urls)),
]