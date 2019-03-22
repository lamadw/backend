# Generated by Django 2.1.7 on 2019-03-18 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_course_instructorname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructorname',
        ),
        migrations.RemoveField(
            model_name='hwincourse',
            name='instructorname',
        ),
        migrations.RemoveField(
            model_name='hwincourse',
            name='superviser',
        ),
        migrations.AddField(
            model_name='hwincourse',
            name='instructor',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courseinstructure',
            name='instructorname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hwincourse',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hwincourse',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentincourse',
            name='studentName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]