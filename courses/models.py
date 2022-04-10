from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        abstract = True
        ordering = ['updated_at', 'created_at']


class Lecture(CommonInfo):
    lecture_name = models.CharField(
        max_length=100,
        verbose_name='lecture_name'
    )
    lecture_text = models.TextField(
        blank=True,
        null=True,
        verbose_name='lecture_text'
    )
    


class Test(CommonInfo):
    test_name = models.CharField(
        max_length=100,
        verbose_name='test_name'
    )
    question = models.JSONField()
    answer = models.JSONField()


class Course(CommonInfo):
    stage_num = models.IntegerField(
        verbose_name='stage_num',
        unique=True
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
    )


class Result(CommonInfo):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
        )

    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE
        )
    lecture_active = models.BooleanField()

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
        )
    test_active = models.BooleanField()
    answer = models.JSONField()
    assignment = models.BooleanField()

    @property
    def available_stage(self):
        if not self.test_active:
            return self.lecture
        return self.test

