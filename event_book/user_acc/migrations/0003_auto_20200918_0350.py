# Generated by Django 3.0.7 on 2020-09-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_acc', '0002_auto_20200917_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='phone'),
        ),
    ]