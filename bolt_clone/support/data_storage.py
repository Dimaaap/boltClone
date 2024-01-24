from dataclasses import dataclass


@dataclass
class DataStorage:
    CATEGORIES_LIST = ("Інформація про доставку", "Додаток і властивості", "Дохід та виплати",
                       "Обліковий запис та дані", "Про Bolt Food", "Проблеми з активним замовленням",
                       "Технічні шоколадки")