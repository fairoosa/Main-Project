# Generated by Django 4.1.7 on 2023-03-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0004_alter_newsportal_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsportal',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
