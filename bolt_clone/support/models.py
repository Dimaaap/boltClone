import uuid

from django.db import models
from django.urls import reverse


class ArticleCategories(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    category_title = models.CharField(max_length=170)

    def __str__(self):
        return self.category_title


class Articles(models.Model):
    class Meta:
        ordering = ["article_title"]

    article_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    article_title = models.CharField(max_length=120, default="")
    article_text = models.TextField()
    article_category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE,
                                         related_name="articles")

    def __str__(self):
        return f'{self.article_title} {self.article_category}'

    def get_absolute_url(self):
        return reverse('article', args=[str(self.article_id)])
