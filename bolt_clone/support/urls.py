from django.urls import path

from .views import *

urlpatterns = [
    path('', main_support_view, name='index_support'),
    path('article/<str:article_id>', get_article_page, name="article"),
    path('article/category/<str:category_id>', get_all_category_articles, name="all_category_articles")
]