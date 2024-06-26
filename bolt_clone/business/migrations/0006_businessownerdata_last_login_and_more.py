# Generated by Django 4.2.7 on 2024-04-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_alter_businessownerdata_company_employees_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessownerdata',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='businessownerdata',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
