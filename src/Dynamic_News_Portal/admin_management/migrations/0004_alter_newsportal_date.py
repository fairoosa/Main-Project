# Generated by Django 4.1.7 on 2023-03-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0003_alter_newsportal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsportal',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]