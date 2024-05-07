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
    PROMO_CODES = [
        "2ASDE123",
        "FKAOWLAS",
        "980NMNK1",
        "JINSU400",
        "UWYE12NC",
        "YERMSIW2",
        "89431SNC",
        "NASDNKI2",
        "JKJ1KZXC",
        "897ADNMC"
    ]

    DRIVE_AND_TIME_CHOICE = (
        ("", ""),
        ("only_work_day", "Тільки будні"),
        ("user_settings", "Налаштування користувачів")
    )

    TRACK_COSTS = (
        ("", ""),
        ("cost_notice", "Нотатка про витрати"),
        ("cost_code", "Код витрат")
    )

    COSTS_AMOUNT_CONTROL = (
        ("", ""),
        ("individual_level", "Індивідувальний рівень"),
        ("group_level", "Груповий рівень")
    )

    DRIVE_PLACES = (
        ("", ""),
        ("to_from_certain_locations", "До або з певних локацій"),
        ("only_from_locations", "Тільки з певних локацій"),
        ("only_to_locations", "Тільки до певних локацій"),
        ("between_locations", "Між певними локаціями")
    )

    LOCATION_RADIUS = (
        ("0.5", "0.5км"),
        ("1", "1км"),
        ("1.5", "1.5км"),
        ("2", "2км"),
        ("2.5", "2.5км"),
        ("3", "3км"),
        ("3.5", "3.5км"),
        ("4", "4км"),
        ("4.5", "4.5км"),
        ("5", "5км"),
        ("10", "10км"),
        ("20", "20км"),
        ("30", "30км"),
        ("40", "40км"),
        ("50", "50км"),
        ("60", "60км"),
        ("70", "70км"),
        ("80", "80км"),
        ("90", "90км"),
        ("100", "100км")
    )

    BOLT_SERVICES = (
        ("https://business.bolt.eu/current/assets/img/policies/bolt-401b44b687c7d62e8d9793b13dcea9cb.png",
         "Bolt", "Надійні та універсальні для повсякденних транспортних потреб"),
        ("https://business.bolt.eu/current/assets/img/policies/xl-2417ecd9e197ae8cf1278d5faeb90f9e.png",
         "XL", "Доступні поїздки до 6 осіб"),
        ("https://business.bolt.eu/current/assets/img/policies/comfort-7a948795cb347ce8cf10563bf08153fd.png",
         "Comfort", "Більш комфортні автомобілі з найкращими водіями"),
        ("https://business.bolt.eu/current/assets/img/policies/business-0929a7c1acd5aabb7e61dc6543d27a41.png",
         "Business", "Елегантні поїздки з нашими автомобілями бізнес-класу"),
        ("https://business.bolt.eu/current/assets/img/policies/premium-84a4d0728cd5c221d7f6de7c39fcce07.png",
         "Premium", "Найкращі у класі ТЗ"),
        ("https://business.bolt.eu/current/assets/img/policies/two_three_wheelers-68a5cb4499453071dc7add410ad6e2f3.png",
         "Дво- або триколісні автомобілі", "Ефектні та спритні автоматичні рікши/мотоцикли"),
        ("https://business.bolt.eu/current/assets/img/policies/bolt_send-28509d9d90b89c379a8cc0c4b95cd10a.png",
         "Delivery", "Швидка доставка"),
        ("https://business.bolt.eu/current/assets/img/policies/scooters-c9f3730f05a657b947b01bf21cf9cb1f.png",
         "Електросамокати", "Двоколісні, дружні до довкілля подорожі"),
        ("https://business.bolt.eu/current/assets/img/policies/drive-ea4321ef40e746477768908e0997d00c.png",
         "Bolt Drive", "Автопрокат для вашої команди")
    )

    RADIUS = (
        ("0.5", "0.5км"),
        ("1", "1км"),
        ("1.5", "1.5км"),
        ("2", "2км"),
        ("2.5", "2.5км"),
        ("3", "3км"),
        ("3.5", "3.5км"),
        ("4", "4км"),
        ("4.5", "4.5км"),
        ("5", "5км"),
        ("10", "10км"),
        ("20", "20км"),
        ("30", "30км"),
        ("40", "40км"),
        ("50", "50км"),
        ("60", "70км"),
        ("80", "80км"),
        ("90", "90км"),
        ("100", "100км")
    )
