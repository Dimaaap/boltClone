# Generated by Django 4.2.7 on 2024-01-08 12:59

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
            name='City',
            fields=[
                ('city_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city_title', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CourierMainInfo',
            fields=[
                ('courier_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('courier_first_name', models.CharField(max_length=140)),
                ('courier_last_name', models.CharField(max_length=180)),
                ('courier_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('courier_email', models.EmailField(max_length=130)),
                ('courier_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.city')),
            ],
        ),
    ]
