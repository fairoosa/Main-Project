# Generated by Django 4.1.7 on 2023-03-11 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsportal',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 20, 31, 41, 525973)),
        ),
    ]