# Generated by Django 3.0.2 on 2020-01-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint_calculator', '0011_auto_20200130_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='result',
        ),
    ]
