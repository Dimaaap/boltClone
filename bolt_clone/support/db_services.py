import os

from django.core.exceptions import ObjectDoesNotExist

from .data_storage import DataStorage
from .models import ArticleCategories, Articles
from .filters import EqualFilter

data_storage = DataStorage()


def get_all_from_model(model):
    return model.objects.all()


def get_method_in_model(model, field: str, value: str):
    eq_filter = EqualFilter()
    try:
        field = model.objects.get(**eq_filter(field, value))
    except ObjectDoesNotExist:
        return False
    return field


def filter_fields_in_model(model, field: str, value: str):
    eq_filter = EqualFilter()
    return model.objects.filter(**eq_filter(field, value))


def insert_data_in_categories_db():
    for category in data_storage.CATEGORIES_LIST:
        ArticleCategories.objects.create(category_title=category)


def text_insert_article_in_db():
    module_dir = os.path.dirname(__file__)
    category = ArticleCategories.objects.get(category_title="Інформація про доставку")
    file_path = os.path.join(module_dir, 'articles_mark/end_delivery_process.txt')
    with open(file_path, "r", encoding="utf8") as text_file:
        data = text_file.read()
    Articles.objects.create(article_title="Завершення процесу доставки", article_text=data,
                            article_category=category)

# FILES_LIST = {
#     'unsubscribe_from_spam': "Я хочу відписатися від розсилки",
#     'update_account_data': "Я хочу оновити дані свого облікового запису",
# }
#
#
# def insert_article_in_db():
#     module_dir = os.path.dirname(__file__)
#     category = ArticleCategories.objects.get(category_title="Обліковий запис та дані")
#     for file in FILES_LIST:
#         file_path = os.path.join(module_dir, f"articles_mark/account_and_data/{file}")
#         with open(file_path, "r", encoding="utf8") as text_file:
#             data = text_file.read()
#         Articles.objects.create(article_title=FILES_LIST[file], article_text=data,
#                                 article_category=category)
