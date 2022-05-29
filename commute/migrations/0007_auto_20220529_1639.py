# Generated by Django 2.1.5 on 2022-05-29 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commute', '0006_auto_20220529_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='commute',
            name='user_major',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='학과'),
        ),
        migrations.AlterField(
            model_name='commute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
