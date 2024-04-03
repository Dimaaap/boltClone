from dataclasses import dataclass


@dataclass
class DataStorage:
    EMPLOYEES_COUNT = (
        "Від 1 до 25",
        "Від 26 до 100",
        "Від 101 до 250",
        "Понад 251"
    )
    COUNTRY_LIST = (
        ("🇦🇹", "Австрія"),
        ("🇦🇿", "Азербайджан"),
        ("🇧🇪", "Бельгія"),
        ("🇬🇧", "Велика Британія"),
        ("🇬🇭", "Гана"),
        ("🇬🇪", "Грузія"),
        ("🇪🇪", "Естонія"),
        ("🇮🇪", "Ірландія"),
        ("🇪🇸", "Іспанія"),
        ("🇨🇾", "Кіпр"),
        ("🇱🇻", "Латвія"),
        ("🇱🇹", "Литва"),
        ("🇲🇹", "Мальта"),
        ("🇲🇽", "Мексика"),
        ("🇳🇬", "Нігерія"),
        ("🇳🇱", "Нідерланди"),
        ("🇩🇪", "Німеччина"),
        ("🇳🇴", "Норвегія"),
        ("🇵🇾", "Парагвай"),
        ("🇿🇦", "Південно-Африканська Республіка"),
        ("🇵🇱", "Польща"),
        ("🇵🇹", "Португалія"),
        ("🇷🇴", "Румунія"),
        ("🇸🇦", "Саудівська Аравія"),
        ("🇸🇰", "Словаччина"),
        ("🇹🇭", "Таїланд"),
        ("🇹🇿", "Танзанія"),
        ("🇹🇳", "Туніс"),
        ("🇺🇬", "Уганда"),
        ("🇭🇺", "Угорщина"),
        ("🇺🇦", "Україна"),
        ("🇭🇷", "Хорватія"),
        ("🇨🇿", "Чехія"),
        ("🇸🇪", "Швеція")
    )