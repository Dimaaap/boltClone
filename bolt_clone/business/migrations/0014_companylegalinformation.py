# Generated by Django 4.2.7 on 2024-04-11 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_businessownerdata_is_email_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyLegalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_legal_name', models.CharField(default='', max_length=250)),
                ('bills_email', models.EmailField(default='', max_length=150)),
                ('company_address', models.CharField(default='', max_length=200)),
                ('edrpou_data', models.CharField(default='', max_length=8)),
                ('company_ipn', models.CharField(default='', max_length=12)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
