# Generated by Django 4.2.7 on 2024-02-08 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_countryzones_drivercountries_country_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='driver_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='driver.drivercities'),
        ),
    ]
