# Generated by Django 4.2.7 on 2024-01-19 06:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategories',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('article_slug', models.SlugField(default='')),
                ('article_title', models.CharField(default='', max_length=120)),
                ('article_text', models.TextField()),
                ('article_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.articlecategories')),
            ],
        ),
    ]
