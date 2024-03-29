# Generated by Django 2.1.7 on 2019-03-19 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provedinstuctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='requestinstuctor',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='provedinstuctor',
            name='requestinstuctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructure.requestinstuctor'),
        ),
    ]
