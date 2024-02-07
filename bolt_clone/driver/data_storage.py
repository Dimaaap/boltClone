from dataclasses import dataclass


@dataclass
class DataStorage:
    COUNTRY_ZONES_LIST = ["Африка", "Азія", "Європа", "Латинська Америка"]
    COUNTRIES_LIST = {
        "Африка": [
            ("🇨🇲", "Камерун"),
            ("🇬🇭", "Гана"),
            ("🇰🇪", "Кенія"),
            ("🇲🇱", "Малі"),
            ("🇰🇪", "Мозамбік"),
            ("🇳🇦", "Намібія"),
            ("🇳🇬", "Нігерія"),
            ("🇿🇦", "Південно-Африканська Республіка"),
            ("🇹🇳", "Туніс"),
            ("🇺🇬", "Уганда"),
            ("🇹🇿", "Танзанія"),
            ("🇿🇲", "Замбія"),
            ("🇿🇼", "Зімбабве")
        ],
        "Азія": [
            ("🇮🇶", "Ірак"),
            ("🇱🇧", "Ліван"),
            ("🇳🇵", "Непал"),
            ("🇸🇦", "Саудівська Аравія"),
            ("🇹🇭", "Таїланд"),
        ],
        "Європа": [
            ("🇦🇹", "Австрія"),
            ("🇦🇿", "Азербайджан"),
            ("🇧🇪", "Бельгія"),
            ("🇭🇷", "Хорватія"),
            ("🇨🇾", "Кіпр"),
            ("🇨🇿", "Чехія"),
            ("🇩🇰", "Данія"),
            ("🇪🇪", "Естонія"),
            ("🇫🇮", "Фінляндія"),
            ("🇫🇷", "Франція"),
            ("🇬🇪", "Грузія"),
            ("🇩🇪", "Німеччина"),
            ("🇭🇺", "Угорщина"),
            ("🇮🇪", "Ірландія"),
            ("🇮🇹", "Італія"),
            ("🇱🇻", "Латвія"),
            ("🇱🇹", "Литва"),
            ("🇲🇹", "Мальта"),
            ("🇲🇩", "Молдова"),
            ("🇳🇱", "Нідерланди"),
            ("🇳🇴", "Норвегія"),
            ("🇵🇱", "Польща"),
            ("🇵🇹", "Португалія"),
            ("🇷🇴", "Румунія"),
            ("🇸🇰", "Словаччина"),
            ("🇸🇮", "Словенія"),
            ("🇪🇸", "Іспанія"),
            ("🇸🇪", "Швеція"),
            ("🇨🇭", "Швейцарія"),
            ("🇬🇧", "Великобританія"),
            ("🇬🇧", "Україна")
        ],
        "Латинська Америка": [
            ("🇪🇨", "Еквадор"),
            ("🇸🇻", "Ель Сальвадор"),
            ("🇲🇽", "Мексика"),
            ("🇵🇾", "Парагвай")
        ]
    }
    CITIES_LIST = {
        "Камерун": [
            "Дуала"
        ],
        "Гана": [
            "Аккра", "Го", "Кумасі", "Кейп-Кост", "Кофорідуа", "Суньяні",
            "Томале", "Секонді-Такораді"
        ],
        "Кенія": [
            "Діані", "Елдорет", "Ембу", "Какамега", "Каратіна", "Кіліфі",
            "Кісуму", "Кітале", "Малінді", "Меру", "Момбаса", "Найробі",
            "Найваша", "Накуру", "Нанюкі", "Ньєрі", "Тіка"
        ],
        "Малі": [
            "Бамако"
        ],
        "Мозамбік": [
            "Мапуту"
        ],
        "Намібія": [
            "Віндгук"
        ],
        "Нігерія": [
            "Аба", "Абакалікі", "Абеокута", "Абуджа",
            "Адо-Екіті", "Акуре", "Асаба", "Авка",
            "Баучі", "Бенін-Сіті", "Калабар", "Енугу",
            "Ібадан", "Ілорин", "Джос", "Кадуна", "Кано",
            "Лафіа", "Лагос", "Локоджа", "Макурді", "Нневі",
            "Нсукка", "Ондо", "Оніча", "Ошогбо", "Оверрі",
            "Порт-Харкурт", "Умуахія", "Уйо", "Варрі", "Єнагоа",
            "Зарія"
        ],
        "Південно-Африканська Республіка": [
            "Кейптаун", "Дурбан", "Іст-Лондон", "Емалахлені",
            "Ермело", "Гарден-Рут", "Гремстаун (Маханда)",
            "Йоганнесбург", "Кімберлі", "Мбомбела", "Умтата",
            "Пхутхадітжхаба", "Пітермаріцбург", "Полокване",
            "Порт-Елізабет", "Почефструм", "Преторія", "Квінстаун",
            "Рустенбург", "Тхохояндоу", "Апінгтон", "Велком", "Вустер"
        ],
        "Туніс": [
            "Сус", "Туніс"
        ],
        "Уганда": [
            "Гулу", "Кампала", "Мбарара"
        ],
        "Танзанія": [
            "Аруша", "Дар-ес-Салаам",
            "Додома", "Мванза"
        ],
        "Замбія": [
            "Лусака"
        ],
        "Зімбабве": [
            "Хараре"
        ],
        "Ірак": ["Багдад"],
        "Ліван": ["Бейрут"],
        "Непал": ["Катманду"],
        "Саудівська Аравія": [
            "Провінція Ель-Баха", "Провінція Ель-Джауф", "Мінтака Ель-Касім",
            "Провінція Асір", "Східна мінтака", "Провінція Хаіль", "Провінція Джізан",
            "Мінтака Мекка", "Мінтака Ель-Медина", "Провінція Наджран", "Північна провінція",
            "Мінтака Ер-Ріяд", "Південня Мінтака", "Провінція Табук"
        ],
        "Таїланд": [
            "Бангкок", "Чіанг-Май", "Чіанграй", "Хон Каен", "Накхонратчасіма", "Пхукет",
            "Удонтхані"
        ],
        "Австрія": [
            "Айзенштадт", "Грац", "Нойзідль-ам-Зее",
            "Парндорф", "Подерсдорф-ам-Зее", "Руст",
            "Зальцбург", "Відень"
        ],
        "Азербайджан": [
            "Баку", "Гянджа", "Ленкорань", "Мінгечаур", "Гебеле",
            "Шекі", "Шамкір", "Сумгаїт"
        ],
        "Бельгія": [
            "Антверпен", "Брюссель", "Гент", "Левен"
        ],
        "Хорватія": [
            "Дубровнік", "Карловац", "Осієк", "Пула",
            "Рієка", "Спліт", "Задар", "Загреб", "Шибеник"
        ],
        "Кіпр": [
            "Ая-Напа", "Фамагуста", "Ларнака", "Лімасол", "Нікосія",
            "Пафос"
        ],
        "Чехія": [
            "Босковіце", "Брно", "Хеб", "Фрідек-Містек", "Гавіржов",
            "Градець-Кралове", "Яблонець-над-Нисою", "Їглава", "Карлові Вари",
            "Карвіна", 'Кладно', "Кралупи-на-Влтаві", "Ліберець", "Млада Болеслав",
            "Новий Їчин", "Оломоуць", "Острава", "Пардубіце", "Плзень", "Прага",
            "Простейов", "Пржибрам", "Табор", "Чеське Будейовіце"
        ],
        "Данія": ["Копенгаген"],
        "Естонія": [
            "Хаапсалу", "Йихві", "Кохтла-Ярве", "Курессааре", "Нарва",
            "Пярну", "Раквере", "Таллінн", "Тарту", "Вільянді", "Виру"
        ]
    }