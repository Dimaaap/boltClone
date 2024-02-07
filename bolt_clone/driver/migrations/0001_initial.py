# Generated by Django 4.2.7 on 2024-02-07 13:27

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('driver_email', models.EmailField(max_length=100, unique=True)),
                ('driver_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='DriverCountries',
            fields=[
                ('country_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country_title', models.CharField(default='', max_length=50)),
                ('country_emoji_flag', models.CharField(blank=True, default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DriverCities',
            fields=[
                ('city_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city_title', models.CharField(blank=True, default='', max_length=120)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.drivercountries')),
            ],
        ),
    ]