# Generated by Django 3.0.7 on 2020-09-17 20:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
