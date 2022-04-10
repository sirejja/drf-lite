from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from courses.models import (
    Lecture, Test, Course, Result, User
)
from courses.serializers import (
    ResultStudentSerializer, CourseStudentSerializer,
    LectureStudentSerializer, TestStudentSerializer, UserSerializer
)
from courses.mixins import StudentMixin

class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ResultApi(APIView, StudentMixin):
    def get(self, request, *args, **kwargs):
        model_data = Result.objects.prefetch_related('lecture').filter(student__id=request.user.id)
        data = {}
        if model_data:
            data = ResultStudentSerializer(model_data, many=True).data
        return Response(data)


class StudentLecture(APIView, StudentMixin):
    def get(self, request, *args, **kwargs):
        model_data = Result.objects.filter(
            student__id=request.user.id
        ).select_related('lecture')
        if model_data and model_data.get('lecture_active'):
            return Response(LectureStudentSerializer(model_data, many=True).data)

    def post(self, request, *args, **kwargs):
        model_data = Result.objects.filter(
            student__id=request.user.id
        ).select_related('lecture')


class StudentTest(APIView, StudentMixin):
    def get(self, request, *args, **kwargs):
        model_data = Result.objects.filter(
            student__id=request.user.id
        ).select_related('test')
        if model_data:
            return Response(TestStudentSerializer(model_data, many=True).data)


class StudentCourse(APIView, StudentMixin):
    def get(self, request, *args, **kwargs):
        model_data = Course.objects.select_related('test').select_related('lecture')
        if model_data:
            return Response(CourseStudentSerializer(model_data, many=True).data)

