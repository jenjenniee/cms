# Generated by Django 2.1.5 on 2022-05-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commute', '0008_remove_commute_user_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_department', models.CharField(blank=True, max_length=20, null=True, verbose_name='부서')),
                ('user_profile', models.ImageField(blank=True, upload_to='', verbose_name='프로필 사진')),
            ],
        ),
    ]