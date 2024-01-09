from dataclasses import dataclass


@dataclass
class DataStorage:
    cities = ["Київ", "Львів", "Вінниця", "Бровари", "Дніпро", "Одеса", "Харків"]
    fleets = ["Kyiv Fleet 01", "Kyiv Fleet 02"]
    delivery_methods = ["Автомобіль", "Велосипед", "Мотоцикл", "Пішки"]
    has_bag = (("1", "У мене є своя сумка для доставок(іншого кольору)"),
               ("2", "Я хочу отримати фірмову термосумку для доставок Bolt Food"))
    is_adult = [("1", "Підтверджую")]
    is_agree_with_sms = [("1", "Погоджуюсь")]

