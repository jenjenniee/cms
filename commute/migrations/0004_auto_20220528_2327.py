# Generated by Django 2.1.5 on 2022-05-28 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commute', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='학번')),
            ],
        ),
        migrations.AlterField(
            model_name='commute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commute.User'),
        ),
    ]
