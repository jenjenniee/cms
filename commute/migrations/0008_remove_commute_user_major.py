# Generated by Django 2.1.5 on 2022-05-29 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute', '0007_auto_20220529_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commute',
            name='user_major',
        ),
    ]
