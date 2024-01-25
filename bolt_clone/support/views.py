from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Articles, ArticleCategories
from .db_services import get_all_from_model, get_method_in_model, filter_fields_in_model


def main_support_view(request):
    search_result_query = request.GET.get("q")
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if search_result_query:
            articles = Articles.objects.filter(article_title__icontains=search_result_query)
            data = [{"title": article.article_title, 'content': article.article_text} for article in articles]
            print(articles)
        else:
            data = {'error': 'За запитом нічого не знайдено'}
        return JsonResponse(data, safe=False)
    else:
        if search_result_query:
            articles = Articles.objects.filter(article_title__icontains=search_result_query)
        else:
            articles = ""
        categories_list = get_all_from_model(ArticleCategories)
        context = {"categories": categories_list, "articles": articles}
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


def search_articles(request):
    return render(request, "support/search_article_page.html ")
