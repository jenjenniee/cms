# Generated by Django 4.0.4 on 2022-06-03 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]