# Generated by Django 4.1.7 on 2023-03-30 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0005_newsportal_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsportal',
            old_name='name',
            new_name='portal_name',
        ),
    ]
