# Generated by Django 3.2rc1 on 2021-03-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(choices=[('Argentina', 57.3), ('Australia', 65.1), ('Austria', 19.0), ('Belgium', 13.9), ('Brazil', 14.1), ('Canada', 19.6), ('Caribbean region', 64.0), ('Chile', 56.0), ('China', 72.3), ('China (Hong Kong)', 93.3), ('Colombia', 15.5), ('Costa Rica', 16.1), ('Czech Republic', 29.7), ('Egypt', 67.8), ('France', 6.6), ('Germany', 20.8), ('India', 103.1), ('Indonesia', 126.7), ('Ireland', 30.0), ('Italy', 24.9), ('Japan', 75.5), ('Jordan', 98.3), ('Malaysia', 92.6), ('Mexico', 30.3), ('Netherlands', 21.7), ('New Zealand', 12.3), ('Panama', 31.1), ('Poland', 53.8), ('Portugal', 19.2), ('Qatar', 140.9), ('Russian Federation', 38.7), ('Saudi Arabia', 108.5), ('Singapore', 48.4), ('South Africa', 62.2), ('South Korea', 80.3), ('Spain', 23.5), ('Switzerland', 8.9), ('Thailand', 64.7), ('Turkey', 56.6), ('United Arab Emirates', 117.0), ('United Kingdom', 26.4), ('United States', 25.6), ('Vietnam', 63.5)], max_length=60, verbose_name='Kraj zakwaterowania'),
        ),
    ]
