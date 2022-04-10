from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# TODO fix me
urlpatterns = [
    path('register', views.CreateUserView.as_view()),
    path('auth/', obtain_auth_token),
    
    path('result', views.ResultApi.as_view()),
    path('lecture', views.StudentLecture.as_view()),
    path('test', views.StudentTest.as_view()),
    path('course', views.StudentCourse.as_view()),
    
]
