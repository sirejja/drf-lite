from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from courses import views

router = routers.DefaultRouter()

base_path = 'api/'
# TODO fix me
urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_path, include('courses.urls')),
]
