# Generated by Django 4.0.3 on 2022-04-08 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_test_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='answer',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]