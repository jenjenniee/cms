# Generated by Django 4.0.4 on 2022-06-03 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]