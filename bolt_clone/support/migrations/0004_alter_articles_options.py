# Generated by Django 4.2.7 on 2024-01-23 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_alter_articles_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['article_title']},
        ),
    ]
