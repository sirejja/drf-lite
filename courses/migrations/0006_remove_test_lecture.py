# Generated by Django 4.0.3 on 2022-04-08 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_courses_course_rename_lectures_lecture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='lecture',
        ),
    ]
