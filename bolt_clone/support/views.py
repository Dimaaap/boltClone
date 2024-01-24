from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from .models import Articles, ArticleCategories
from .db_services import get_all_from_model, get_method_in_model, filter_fields_in_model


def main_support_view(request):
    categories_list = get_all_from_model(ArticleCategories)
    context = {"categories": categories_list}
    return render(request, "support/main_support_page.html", context)


def get_article_page(request, article_id):
    article = get_method_in_model(Articles, "article_id", article_id)
    if not article:
        return redirect(main_support_view)
    context = {"article": article}
    return render(request, "support/article_page.html", context)


def get_all_category_articles(request, category_id):
    category = get_method_in_model(ArticleCategories, "category_id", category_id)
    if not category:
        return redirect(main_support_view)
    articles = filter_fields_in_model(Articles, "article_category", category)
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {"category": category, "articles": articles, "page_obj": page_obj}
    return render(request, "support/all_category_articles_page.html", context)