from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Articles, ArticleCategories


def main_support_view(request):
    categories_list = ArticleCategories.objects.all()
    context = {"categories": categories_list}
    return render(request, "support/main_support_page.html", context)


def get_article_page(request, article_id):
    try:
        article = Articles.objects.get(article_id=article_id)
    except ObjectDoesNotExist:
        return redirect(main_support_view)
    context = {"article": article}
    return render(request, "support/article_page.html", context)


def get_all_category_articles(request, category_id):
    try:
        category = ArticleCategories.objects.get(category_id=category_id)
    except ObjectDoesNotExist:
        print("here")
        return redirect(main_support_view)
    context = {"category": category}
    return render(request, "support/all_category_articles_page.html", context)