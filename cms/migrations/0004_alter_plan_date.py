# Generated by Django 4.0.4 on 2022-06-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='date',
            field=models.DateField(),
        ),
    ]