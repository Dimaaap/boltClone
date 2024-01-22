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


FILES_LIST = {'cant_enter_app': "Я не можу увійти в додаток",
              'tech_problem': "У мене виникла технічна проблема",
              'dont_pay_cash_orders.txt': "Я не отримую готівкових запитів на доставку",
              'cant_get_notifications.txt': "Я не отримую сповіщень з додатка"}


def insert_article_in_db():
    module_dir = os.path.dirname(__file__)
    category = ArticleCategories.objects.get(category_title="Технічні неполадки")
    for file in FILES_LIST:
        file_path = os.path.join(module_dir, f"articles_mark/tech_bugs/{file}")
        with open(file_path, "r", encoding="utf8") as text_file:
            data = text_file.read()
        Articles.objects.create(article_title=FILES_LIST[file], article_text=data,
                                article_category=category)
