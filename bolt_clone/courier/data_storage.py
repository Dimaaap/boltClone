from dataclasses import dataclass


@dataclass
class DataStorage:
    cities = ["Київ", "Львів", "Вінниця", "Бровари", "Дніпро", "Одеса", "Харків"]
    fleets = ["Kyiv Fleet 01", "Kyiv Fleet 02"]
    is_adult = [("1", "Підтверджую")]
    is_agree_with_sms = [("1", "Погоджуюсь")]

