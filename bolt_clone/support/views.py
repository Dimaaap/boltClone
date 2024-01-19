from django.shortcuts import render
from .models import Articles, ArticleCategories


def main_support_view(request):
    categories_list = ArticleCategories.objects.all()
    context = {"categories": categories_list}
    return render(request, "support/main_support_page.html", context)
