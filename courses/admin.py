from django.contrib import admin
from courses.models import (
    Lecture, Test, Course, Result
)

admin.site.register(Result)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Lecture)
