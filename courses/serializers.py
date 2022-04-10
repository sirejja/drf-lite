from rest_framework import serializers
from courses.models import Lecture, Test, Course, Result, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ["id", "username", "password"]


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['lecture_name', 'lecture_text']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['test_name', 'question']
        
class ResultStudentSerializer(serializers.ModelSerializer):
    pass

class CourseStudentSerializer(serializers.ModelSerializer):
    class LectureSerializer(serializers.Serializer):
        lecture_name = serializers.CharField(max_length=200)
        created_at = serializers.DateTimeField()
    class TestSerializer(serializers.Serializer):
        test_name = serializers.CharField(max_length=200)
        created_at = serializers.DateTimeField()

    lecture = LectureSerializer()
    test = TestSerializer()
    
    class Meta:
        model = Course
        fields = ['test', 'lecture']


class LectureStudentSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer()
    class Meta:
        model = Result
        fields = ['lecture']


class TestStudentSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    class Meta:
        model = Result
        fields = ['test']

