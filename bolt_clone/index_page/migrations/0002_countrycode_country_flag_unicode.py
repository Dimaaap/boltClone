# Generated by Django 4.2.7 on 2023-12-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrycode',
            name='country_flag_unicode',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
