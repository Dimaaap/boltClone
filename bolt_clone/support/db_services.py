import os
from .models import ArticleCategories, Articles

CATEGORIES_LIST = ("Інформація про доставку", "Додаток і властивості", "Дохід та виплати",
                   "Обліковий запис та дані", "Про Bolt Food", "Проблеми з активним замовленням",
                   "Технічні шоколадки")


def insert_data_in_categories_db():
    for category in CATEGORIES_LIST:
        ArticleCategories.objects.create(category_title=category)


def text_insert_article_in_db():
    module_dir = os.path.dirname(__file__)
    category = ArticleCategories.objects.get(category_title="Інформація про доставку")
    file_path = os.path.join(module_dir, 'articles_mark/end_delivery_process.txt')
    with open(file_path, "r", encoding="utf8") as text_file:
        data = text_file.read()
    Articles.objects.create(article_title="Завершення процесу доставки", article_text=data,
                            article_category=category)


FILES_LIST = {'bolt_bag_store': "Зберігання сумки Bolt",
              'comments_check': "Перевірка коментарів по доставці",
              'packing': "Пакування"}


def insert_article_in_db():
    module_dir = os.path.dirname(__file__)
    category = ArticleCategories.objects.get(category_title="Інформація про доставку")
    for file in FILES_LIST:
        file_path = os.path.join(module_dir, f"articles_mark/delivery_info/{file}")
        with open(file_path, "r", encoding="utf8") as text_file:
            data = text_file.read()
        Articles.objects.create(article_title=FILES_LIST[file], article_text=data,
                                article_category=category)
