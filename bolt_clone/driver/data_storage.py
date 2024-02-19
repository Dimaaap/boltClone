from dataclasses import dataclass

from django.conf import settings


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
        ],
        "Фінляндія": [
            "Еспоо", "Гельсінкі", "Ярвенпяа", "Керава", "Кірконуммі",
            "Клауккала", "Нурміярві", "Оулу", "Сіпоо", "Тампере", "Турку",
            "Туусула", "Вантаа"
        ],
        "Франція": [
            "Аннесі", "Бордо", "Брест", "Кан", "Шамбері", "Клермон-Ферран",
            "Гренобль", "Гавр", "Лілль", "Ліон", "Марсель", "Мец", "Монпельє",
            "Мюлуз", "Нансі", "Нант", "Ніцца", "Нім-Авіньйон", "Орлеан", "Париж",
            "Перпіньян", "Реймс", "Ренн", "Руан", "Сент-Етьєн", "Стрсбург", "Тулон",
            "Тулуза", "Тур"
        ],
        "Грузія": [
            "Бакуріані", "Батумі", "Горі", "Гадаурі та Степанцміда", "Кутаїсі",
            "Поті", "Руставі", "Тбілісі", "Телаві", "Зугдіді"
        ],
        "Німеччина": [
            "Аугсбург", "Берлін", "Бернбург", "Білефельд", "Бохум", "Бонн", "Брауншвейг",
            "Брюль", "Целле", "Кельн", "Дармштадт", "Дортмунд", "Дюссельдорф", "Ерланген",
            "Ессен", "Франкфурт-на-Майні", "Фюрт", "Гельзенкірхен", "Гіфгорн", "Геттінген",
            "Галле", "Гамбург", "Ганновер", "Гейдельберг", "Герфорд", "Гільден", "Гільдесгайм",
            "Карлсруе", "Кассель", "Кіль", "Лаатцен", "Людвігсгафен", "Любек", "Майнц", "Мангайм",
            "Мерзебург", "Мюнхен", "Менхенгладбах", "Мюльгайм-ам-Майн", "Мюнстер", "Нойс",
            "Нюрнберг", "Ольденбург", "Падерборн", "Пайне", "Потсдам", "Ройтлінген", "Зальцгітер",
            "Швабах", "Золінген", "Штасфурт", "Штайн", "Штутгарт", "Тюбінген", "Вісбаден", "Вольфсбург"
        ],
        "Угорщина": [
            "Будапешт", "Дебрецен", "Мішкольц", "Ньїредьгаза", "Печ",
            "Шопрон", "Сегед"
        ],
        "Ірландія": [
            "Брей", "Корк", "Дублін", "Дан Лері", "Кілкенні", "Слайго", "Вексфорд"
        ],
        "Італія": [
            "Мілан", "Модена", "Реджо-нель-Емілія", "Турин"
        ],
        "Латвія": [
            "Даугавпілс", "Єлгава", "Юрмала", "Лієпая", "Огре", "Резекне",
            "Рига", "Саласпілс", "Сігулда", "Тукумс", "Валмієра", "Вентспілс"
        ],
        "Литва": [
            "Алітус", "Друскінінкай", "Йонава", "Каунас", "Казлу-Руда",
            "Кедайняй", "Клайпеда", "Маріямполе", "Мажейкяй", "Ніда",
            "Паланга", "Паневежис", "Таураге", "Тельшяй", "Тракай",
            "Укмерге", "Утена", "Вільнюс", "Шяуляй", "Шилуте"
        ],
        "Мальта": [
            "Гоцо", "Мальта"
        ],
        "Молдова": ["Кишинів"],
        "Нідерланди": [
            "Амстердам", "Ейндговен", "Енсхеде", "Гронінген", "Генгело",
            "Леуварден", "Неймеген", "Роттердам", "Гаага", "Утрехт"
        ],
        "Норвегія": [
            "Берген", "Драммен", "Крістіансанн", "Ліллестрем", "Мосс", "Осло"
        ],
        "Польща": [
            "Білосток", "Б'єльсько-б'яла", "Бидгощ", "Битом", "Хожув",
            "Ченстохова", "Домброва-Гурнича", "Ельблонг", "Гданськ",
            "Гдиня", "Гожув-Велькопольський", "Явожно", "Катовіце", "Кельце",
            "Кошалін", "Краків", "Легніца", "Люблін", "Ольштин", "Ополе",
            "Познань", "Радом", "Руда Шльонська", "Ряшів", "Сілезія",
            "Сопот", "Щецин", "Тарнув", "Торунь", "Тримісто", "Тихи",
            "Варшава", "Вроцлав", "Владиславово", "Влоцлавек", "Забже",
            "Зелена Гура", "Лодзь", "Свідник"
        ],
        "Португалія": [
            "Алгарве", "Авейру", "Бежа", "Брага", "Браганса", "Каштелу-Бранку",
            "Коїмбра", "Евора", "Фару", "Гуарда", "Лейрія", "Лісабон", "Мадейра",
            "Порталегре", "Порту", "Стантарем", "Сетубал", "Віана-ду-Каштелу",
            "Віла Реал", "Візеу"
        ],
        "Румунія": [
            "Алба-Юлія", "Арад", "Бакеу", "Бая-Маре", "Бистриця", "Ботошані",
            "Брашов", "Браїла", "Бухарест", "Бузеу", "Клуж-Напока", "Констанца",
            "Крайова", "Фокшани", "Галац", "Ясси", "Орадя", "П'ятра-Нямц", "Пітешті",
            "Плоєшті", "Римніку-Вилча", "Сату-Маре", "Сібіу", "Сучава", "Тімішоара", "Тульча",
            "Тирговіште", "Тиргу-Жіу", "Тиргу-Муреш", "Валя-Праховей"
        ],
        "Словаччина": [
            "Банська Бистриця", "Бойнице", "Братислава", "Галанта", "Глоговец",
            "Голіч", "Кошице", "Мартін", "Нітра", "П'єштяни", "Попрад", "Пряшів",
            "Прєвідза", "Тренчин", "Трнава", "Зволен", "Жиліна"
        ],
        "Словенія": [
            "Копер", "Любляна", "Марибор"
        ],
        "Іспанія": [
            "Барселона", "Мадрид", "Малага", "Ов'єдо", "Севілья", "Сарагоса"
        ],
        "Швеція": [
            "Бурос", "Енчепінг", "Екільстуна", "Гетеборг", "Гельсінборг",
            "Крістіанстад", "Лінчепінг", "Лунд", "Мальме", "Норччепінг",
            "Стокгольм", "Седертельє", "Треллеборг", "Уппсала", "Вестерос",
            "Еребру"
        ],
        "Швейцарія": [
            "Вінтертур", "Цюрих"
        ],
        "Великобританія": [
            "Бат", "Бірмінгем", "Бристоль", "Кембридж", "Кардіфф",
            "Дербі", "Единбург", "Великий Манчестер", "Гавант", "Лестер",
            "Лондон", "Мілтон-Кінз", "Ньюкасл-апон-Тайн", "Ньюпорт", "Ноттінгем",
            "Пітерборо", "Портсмут", "Віндзор та Мейденхед", "Шеффілд",
            "Саутгемптон", "Вулвергемптон"
        ],
        "Україна": [
            "Біла Церква", "Бориспіль", "Бровари", "Черкаси", "Чернігів",
            "Чернівці", "Дніпро", "Дрогобич", "Ірпінь", "Івано-Франківськ", "Кам'янець-Подільський",
            "Кам'янське", "Харків", "Хмельницький", "Кременчук", "Кропивницький", "Кривий Ріг",
            "Київ", "Луцьк", "Львів", "Мукачево", "Миколаїв", "Новомосковськ", "Одеса", "Полтава",
            "Рівне", "Суми", "Тернопіль", "Трускавець", "Ужгород", "Вінниця", "Вишгород", "Вишневе",
            "Запоріжжя", "Збараж", "Здолбунів", "Житомир"
        ],
        "Еквадор": ["Гуаякіль"],
        "Ель Сальвадор": ["Сан-Сальвадор"],
        "Мексика": [
            "Агуаскальєнтес", "Дуранго", "Гомес-Паласіо", "Гвадалахара",
            "Лос-Мочіс", "Масатлан"
        ],
        "Парагвай": [
            "Асунсьйон", "Каагуасу", "Сьюдад-дель-Есте", "Коронель-Овьєдо",
            "Енкарнасьйон", "Вільярріка"
        ]
    }
    CAR_MODELS = [
        "ACE",
        "Acura",
        "AIWAYS",
        "AKT",
        "Alfa Romeo",
        "Aprilia",
        "Aston Martin",
        "Atlas Zongshen",
        "Atul",
        "Audi",
        "Baic",
        "Bajaj",
        "Baojun",
        "BAW",
        "Benelli",
        "Bentley",
        "Blavalauto",
        "BMW",
        "BMW Alpina",
        "Bolt",
        "Brilliance Auto",
        "BSE",
        "Buick",
        "Buler",
        "BYD",
        "Cadillac",
        "Carver",
        "CF Moto",
        "Changan",
        "Chery",
        "Chevrolet",
        "Chrysler",
        "Citroen",
        "CMC",
        "Coursier",
        "Crossfire",
        "Cupra",
        "CVS",
        "Dacia",
        "Daewoo",
        "Daihatsu",
        "Datsun",
        "Daylong",
        "Dayun",
        "Deco",
        "Demak",
        "Denstar",
        "DFSK",
        "Dinamo",
        "Dodge",
        "DongFeng",
        "DS",
        "Ducati",
        "Exceed",
        "FAW",
        "Fecon",
        "Ferrari",
        "Fiat",
        "Fisker",
        "Ford",
        "Foton",
        "GAC",
        "Geely",
        "General Motors",
        "Gensis",
        "GIO",
        "GMS",
        "GPX",
        "Great Wall",
        "Guangzhou Haojin",
        "GWM",
        "H SEM",
        "HAIMA",
        "Hanway",
        "Haojue",
        "Hartford",
        "Haval",
        "HAWTAI",
        "Hero",
        "Hero Honda",
        "Holden",
        "Honda",
        "Hongqi",
        "Hover",
        "Hozon",
        "HSV",
        "Hummer",
        "Hyundai",
        "Ikco",
        "Infinity",
        "Ingrace",
        "Innoson",
        "Iran Khodro",
        "ISLO",
        "Isuzu",
        "ITALIKA",
        "Iveco",
        "IZUKA",
        "JAC Motors",
        "Jaguar",
        "Jamuna",
        "Jeep",
        "Jetour",
        "Jiagi",
        "Jinbei",
        "Jincheng",
        "JMC",
        "Kantanka",
        "KAWASAKI",
        "KEEWAY",
        "Kenton",
        "Khazar",
        "Kia",
        "Kinetic",
        "KTM",
        "KYMCO",
        "Kymstone",
        "Lada",
        "Lamborghini",
        "Lambretta",
        "Lancia",
        "Land Rover",
        "LDV",
        "Leapmotor",
        "Leopard",
        "LEVC",
        "Lexus",
        "Lifan",
        "Lincoln",
        "Link Tour",
        "LML",
        "London Cab",
        "Lotus",
        "Lynk&Co",
        "Mahindra",
        "Malaguti",
        "Mana",
        "Maruti",
        "Maserati",
        "Maxus",
        "Maybach",
        "Mazda",
        "McLaren Automotive",
        "Mercedes-Benz",
        "Mercury",
        "MG",
        "Micro",
        "MINI",
        "Mitsubishi",
        "MOTO GUZZI",
        "Motostar",
        "MPM motors",
        "MV AGUSTA",
        "Neta",
        "Nio",
        "Nissan",
        "NIU",
        "NO CAR",
        "Opel",
        "Paggio",
        "Preodua",
        "Peugeout",
        "PHP",
        "Piaggio",
        "Plymouth",
        "Polestar",
        "Pontiac",
        "Porsche",
        "Pragya",
        "Proton",
        "Quantum Technologies",
        "Qute",
        "Race",
        "Range Rover",
        "Ravon",
        "Regal",
        "Renault",
        "Renault Samsung",
        "Rio",
        "Road Prince",
        "Roadmaster",
        "Roll-Royce",
        "Rongxing",
        "Rover",
        "Royal Alloy",
        "Royal Enfield",
        "Runner",
        "Saab",
        "SABA",
        "Saic",
        "Saipa",
        "Salti",
        "Samand",
        "SanLG",
        "Saturn",
        "Scion",
        "Scomadi",
        "Seat",
        "Senova",
        "Seres",
        "Shangai",
        "Shineray",
        "Siytto",
        "Skoda",
        "Skywell",
        "SMART",
        "Sonlink",
        "Soueast",
        "Speranza",
        "SsangYong",
        "Star",
        "Strom",
        "Subaru",
        "Suda",
        "Suzuki",
        "Sym",
        "T better",
        "Taiga",
        "TAILG",
        "Tata",
        "Tesla",
        "Test Model",
        "Tobe",
        "Toyota",
        "Tris",
        "Tris, Concode",
        "TRIUMPH",
        "Trumpchi",
        "TVS",
        "Twinco",
        "Um",
        "United",
        "Vauxhall",
        "Vector",
        "Vento",
        "VESPA",
        "VGV",
        "Victor-R",
        "Volga",
        "Volkswagen",
        "Volvo",
        "Vortex",
        "Walton",
        "Weltmeister",
        "Winnonie",
        "Wuling Motors",
        "Xpeng",
        "Yamaha",
        "Yamazuki",
        "ZAZ",
        "Zeekr",
        "Zongshen",
        "Zotye"
    ]
    MODELS_LIST = [
        {"ACE": ["Classic", "Scrambler"]},
        {"Acura": ["CSX", "ILX", "Integra", "MDX", "RDX", "RL", "RLX", "TL", "TLX", "TSX", "ZDX"]},
        {"AIWAYS": ["U5"]},
        {"AKT": ["200 TT"]},
        {"Alfa Romeo": ["147", "156", "159", "166", "Giulia", "Giulietta", "MiTo", "Stelvio", "Tonale"]},
        {"Aprilia", ["ETX", "RS4", "SR", "STX"]},
        {"Aston Martin": ["DBX", "Rapide", "RapideE"]},
        {"Atlas Zongshen": ["Z", "ZS", "ZS80"]},
        {"Atul": ["Rickshaw (Tuktuk)"]},
        {"Audi": [
            "100", "80", "A1", "A1 Sporback", "A2", "A3", "A4", "A4 Allroad", "A5", "A6", "A6 Allroad",
            "A7", "A8", "A8L", "e-tron", "e-tron GT", "e-tron Sportback", "Q2", "Q3", "Q4 e-tron", "Q5",
            "Q5 Sportback", "Q7", "Q8", "R8", "RS 7", "RS3", "RS6", "S3", "S4", "S5", "S6", "S7", "S8", "TT"
        ]},
        {"Baic": [
            "A115", "Ampersand Electric", "BJ", "BJ40", "D20", "EC3", "EU5", "EX360", "M20", "M60",
            "Roam Air", "Senova D20", "Senova D50", "Senova X55", "X 35", "X25", "X3", "X7"
        ]},
        {"Bajaj": [
            "Avenger", "Bajaj 4 Stroke (Tuktuk)", "Boxer", "CT100", "Discover", "Dominar", "NO BIKE",
            "Platina", "Pragya", "Pulsar", "Pulsar NS125", "Qute", "Rickshaw (Tuktuk)", "V12", "V15"
        ]},
        {"Baojun": ["YEP"]},
        {"BAW": ["Reach"]},
        {"Benelli": ["302", "Leoncino", "TNT", "Tornado", "ZenZero"]},
        {"Bentley": ["Arnage", "Bentayga", "Continental", "Continental GT", "Flying Spur", "Mulsanne"]},
        {"Blavalauto": ["Blaval"]},
        {"BMW": [
            "1 series", "116", "118", "2 series", "2 series Active Tourer", "2 series Gran Coupe",
            "2 series Gran Tourer", "216", "218", "220", "225", "280", "3 series", "3 series Gran Turismo",
            "316", "318", "320", "330", "335", "4 series", "4 series Gran Coupe", "418", "420", "430",
            "5 series", "5 series Gran Turismo", "518", "520", "525", "528", "530", "535", "6 series",
            "6 series Gran Coupe", "6 series GT", "630", "640", "7 series", "725", "730", "740", "745",
            "760", "8 series Gran Coupe", "840d", "C 650 GT", "C 650 Sport", "F 650 GS", "F 700 GS", "F 750 GS",
            "F 800 GS", "F 800 R", "F 850 GS", "G 310 GS", "G 310 R", "G 650", "G 650 GS", "G650 X",
            "Gran Turismo 318D", "GS Adventure", "i3", "i4", "i5", "i7", "i8", "iX", "iX 40", "iX1",
            "iX2", "iX3", "K 1200 R", "K 1200 S", "K 1300 R", "K 1600 GT", "K 1600 GTL", "LI 037",
            "M6", "R 1150 R", "R 1200 GS", "R 1200 GS Adventure", "R 1200 R90", "R 1200 RDarkwhite",
            "R 1200 RT", "S 1000 R", "S 1000 XR", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "XM"
        ]},
        {"BMW Alpina": [
            "B3", "B4 Gran Coupe", "B5", "B6 Gran Coupe", "B7", "B8 Gran Coupe", "D3", "D4 Gran Coupe",
            "D5", "XB7", "XD3", "XD4"
        ]},
        {"Bolt": ["Driver", "Pedicab"]},
        {"Brilliance Auto": [
            "BS2", "BS4", 'BS6', "E Class", "FSV/FRV", "Grandor", "H220", "H230", "H230 EV",
            "H3", "H320", "H330", "H530", "M2", "Splendor", "V3", "V5", "V6", "V7"
        ]},
        {"BSE": ["150"]},
        {"Buick": ["Enclave", "Encore", "Envision", "LaCrosse", "Lucerne", "Regal", "Verano"]},
        {"Buler": ["VX150GY", "VX200", "XY 200", "ZF200"]},
        {"BYD": [
            "Atto 3", "D1", "Dolphin", "e1", "e2", "e3", "e5", "E6", "e6 II", "E6Y", "e9 (Han)",
            "F0", "F3", "F4", "F6", "G3", "G6", "Han", "I3", "L3", "QCI-7160A", "S1(Yuan)", "S2 (Yuan Plus)",
            "S6", "Seagull", "Seal", "Song Plus EV", "Tang"
        ]},
        {"Cadillac": [
            "ATS", "ATS-V", "BLS", "Celestiq", "CT4", "CT5", "CT6", "CTS", "CTS-V", "DTS", "DTS-L",
            "Escalade", "Lyriq", "SRX", "STS", "STS-V", "XT4", "XT5", "XT6", "XTS", "XTS-L"
        ]},
        {"Carver": ["BM"]},
        {"CF Moto": ["Qlink Champion", "Qlink Cruiser", "Qlink Legend", "Qlink Ranger"]},
        {"Changan": [
            "A06", "A600EV", "Alsvin (Yuexiang)", "Alsvin V3", "Alsvin V7", "Auchan A600EV",
            "AVATR 11", "AVATR 12", "Benni (BenBen)", "CM8", "CS15", "CS15 EV", "CS35", "CS35 Plus",
            "CS55", "CS55 Plus", "CS75", "CS75 Plus", "CS85", "CS85 Coupe", "CS95", "CX20", "CX70",
            "Eado", "Eado DT", "Eulove", "F70", "Hafei", "Higer", "Ideal", "Jeep", "Joice (Jiexun)",
            "Linmax (Oushang A800)", "Oushan COS1", "Oushan COS3", "Oushan COS5", "Oushan X5",
            "Oushan X7", "Oushan X7 Plus", "Oushan Z6", "Oushang Honor", "Raeton", "Raeton CC",
            "Uni-K", "Uni-T", "UNI-V", "Z-Shine (CX30)"
        ]},
        {"Chery": [
            "A1/Kimo", "A13", "A15", "A5/Elara", "Amulet", "Arizo 3", "Arizzo 5 Plust/GX",
            "Arizzo 5/EX", "Arizzo 6", "Arizzo 7", "Arizzo 8", "Arizzo E5 Raysince",
            "Beat", "Cowin", "CrossEastar", "E5", "Eastar", "Envy", "eQ1", "eQ2",
            "eQ5", "Face", "Flagcloud", "Fora", "Fulwin", "J11", "J3", "Jaecoo",
            "Jaggi", "Jetour X70", "Jetour X90", "Jetour X95", "M11", "New QQ",
            "OMODA", "Oriental Son", "Q22L", "QQ 308", "QQ6", "Queen", "T11",
            "T1X", "Tiggo", "Tiggo 2", "Tiggo 3", "Tiggo 3x", "Tiggo 3xe", "Tiggo 4",
            "Tiggo 5x", "Tiggo 7", "Tiggo 8", "Tigo 8", "V5", "A18/Karry"
        ]},
        {"Chevrolet": [
            "Ace", "Activ", "Agile", "Astra", "Avalanche", "Aveo", "Beat", "Blazer",
            "Blazer", "Bolt", "Bolt EUV", "Camaro", "Caprice", "Captive", "Cavalier",
            "Celta", "Chevy", "Cobalt", "Colorado", "Corsa", "Cruze", "Derby",
            "DMAX", "Epica", 'Equinox', "Equinox EV", "Evanda", "G Vitara SZ",
            "Geo Prizm", "groove", "HHR", "Impala", 'Kalos', "Klan", "Lacetti",
            "Lanos", "Malibu", "Matiz", "Menlo EV", "Monza", "N200", "Nexia",
            "Niva", "Nubira", "Onix", "Optra", "Orlando", "Prisma", "Rezzo",
            "S10", "Sail", "Silverado", "Silverado EV", "Sonic", "Spark", "Spark EV",
            "Spin", "Suburban", "Tacuma", "Tahoe", "Tracker", "Trailblazer",
            "Traverse", "Trax", "Vectra", 'Volt'
        ]},
        {"Chrysler": [
            "200", "300", "300C", "300M", "Aspen", "Daimler", "Dodge", "Grand Voyager",
            "LHS", "Limousine", "Neon", "Pacifica", "PT Cruiser", "Sebring", "Town & Country",
            "Voyager"
        ]},
        {"Citroen": [
            "Berlingo", "Berlingo Multispace", "C-Crosser", "C-Elysee", "C-Zero", "C1", "C3",
            "C3 Aircross", "C3 Picasso", "C4", "C4 Aircross", "C4 Cactus", "C4 Flair", "C4 Picasso",
            "C4 SpaceTourer", "C4 X", "C5", "C5 Aircross", "C6", "C8", "Dispatch", "Dispatch Combi",
            "DS 3", "DS 3 Crossback", "DS 4", "DS 5", "DS 7 Crossback", "DS 9", "DS5",
            "e-Berlingo", "e-C4", "e-C4 X", "e-SpaceTourer", "Elysee", "Grand  C4 Picasso",
            "Grand C4 SpaceTourer", "Jumper", "Jumpy", "Nemo", "Relay", "Saxo", "Spacetourer",
            "Station Wagon", "Xsara", "Xsara Picasso"
        ]},
        {"CMC": ["Z7"]},
        {"Coursier": ["a velo"]},
        {"Crossfire": ["Xz450"]},
        {"Cupra": ["Ateca", "Born", "Formentor", "Leon", "Tavascan"]},
        {"CVS": ["Pragya"]},
        {"Dacia": [
            "Dokker", "Duster", "Jogger", "Lodgy", "Logan", "Logan MCV", "Sandero", "Sandero Stepway",
            "Solenza", "Spring"
        ]},
        {"Daewoo": [
            "Cielo", "Epica", "Espero", "Evanda", "Gentra", "Kalos", "Lacetti", "Lanos", "Leganza",
            "Matiz", 'Nexia', "Nubira", "Prins", "Racer", "Rezzo", "Runna", "Sens", "Tacuma",
            "Tosca", "Winstorm"
        ]},
        {"Daihatsu": [
            "Atrai", "Boon", "Cuore", "Esse", "Materia", "Mira", "Move", "Move Grand", "Rocky",
            "Sirion", "Storia", "Tanto", "Terios", "Trevis", "Wake", "YRV"
        ]},
        {"Datsun": ["Go", "Go +", "mi-DO", "on-DO"]},
        {"Daylong": ["Explorer"]},
        {"Dayun": ["Deviser", "DY100", "Plight", "Roebuck", "Sprout"]},
        {"Deco": ["Super Ace"]},
        {"Demak": ["Transtar 125"]},
        {"Denstar": ["Desperado"]},
        {"DFSK": ["FENGON 580", "Glory 500", "Mini Bus"]},
        {"Dinamo": [
            "Adventure ELITE", "ALIEN-R", "Chopeper 250", "Custom 150", "GALAXY", "KF-racer",
            "MAX-2", "MAX-3", "METRO", "Monkey", "OMEGA", "Rayo 175", "Rayo ELITE", "Renegada 250",
            "RI-350", "Scorpion 200", "Scorpion 250", "SPEED FIRE", "SPORT R1", "SPORT R2", "U5"
        ]},
        {"Dodge": [
            "Activa", "Attitude", "Avenger", 'Aviator', "Caliber", "CB", "CB150R", "CBF", "CBR",
            "CD", "CG", "Challenger", "Charger", "CRF", "Dakota", "Dart", "Dio", "Dream",
            "Durango", "Grand Caravan", "Hornet", "Journey", "Livo", "Magnum", "Navi", "Neon",
            "Nitro", "PCX", "Ram", "Ram 700", "Ram Van", "Stratus", "Tornado", "Trigger", "Vision", "XR"
        ]},
        {"DongFeng": [
            "A30", "AX7", "DFM AX7", "E11K", "EQ6400LF18", "EX-1", "Fengon 5", "Fengon 500", "Fukang ES600",
            "Fukang EV30", "Glory 560", "Glory 580", "H30", "M-NV", "M5 EV", "Rich", "S30", "Seres 3",
            "TS5 Evo", "X-NV"
        ]},
        {"DS": [
            "3", "3 Crossback", "3 Crossback E-Tense", "4", "4 Crossback", "5", "7 Crossback",
            "7 Crossback E-Tense", "9", "9 E-Tense"
        ]},
        {"Ducati": ["Monster 795", "Monster 796"]},
        {"Exeed": ["LX", "TX", "VX"]},
        {"FAW": [
            "Bestune B30", "Bestune B50", "Bestune B70", "Bestune B90", "Bestune E01", "Bestune T33",
            "Bestune T55", "Bestune T77", "Bestune T99", "Bestune X40", "Bestune X80", "CA 6371",
            "CA 7158", "Diandongwu Young Mini EV", "R7", "S80", "T77", "V2", "V5", "V80", "X40"
        ]},
        {"Fekon": ["Bike"]},
        {"Ferrari": ["459 Italia", 'F430', "FF", "CTC4Luso", "Purosangue"]},
        {"Fiat": [
            "500L", "500L Living", "500X", "Albea", "Argo", "Brava", "Bravo", "Croma", "Doblo", "Ducato",
            "Fiorino", "Freemont", "Grande Punto", "Idea", "Linea", "Marea", "Mobi", "Multipla",
            "One Sporting", "One Way", "Palio", "Panda", "Pulse", "Punto", "Qubo", "Rimo", "Ritmo",
            "Scudo", "Sedici", "Silena", "Stilo", "Talento", "Tipo", "Tofash", "Toro", "Turneo",
            "Ulysse", "Uno"
        ]},
        {"Fisker": ["Karma", "Ocean"]},
        {"Ford": [
            "B-Max", "Bronco", "Bronco Sport", "C-Max", "Crown Victoria", "Econoline", "EcoSport",
            "Edge", "Endeavour", "Escape", "Escort", "Everest", "Everest Titanium", "Expedition",
            "Explorer", "F-150", "F-150 Lightning", "Fairmont", "Falcon", "Falcon BFIII XT",
            "Falcon XR6", "Fiesta", "Figo", "Figo Aspire", "Flex", "Focus", "Focus C-Max",
            "Focus electric", "Focus Estate", "Focus ST", "Freedom", "Freestyle", "Fusion", "G6",
            "Galaxy", "Grand C-Max", "Grand Tourneo", "Ikon", "Journey", "Ka", "Ka +",
            "Kuga", "Maverick", "Mondeo", "Mustang", "Mustang Mach-E", "Mustang Yema",
            "Puma", "Ranger", "S-Max", "Taurus", "Territory", "Tourneo", "Transit",
            "Transit Connect", "Transit Custom", "Transit Inva", 'Victoria', "Vignale",
            "Windstar"
        ]},
        {"Foton": ["Gratour"]},
        {"GAC": [
            "Aion ES", "Aion LX", "Aion S", "Aion V", "Aion Y Plus", "Empow", "GN6", "Trumpchi Empow",
            "Trumpchi GA3", "Trumpchi GA4", "Trumpchi GA5", "Trumpchi GA6", "Trumpchi GA8", "Trumpchi GE3",
            "Trumpchi GS3", "Trumpchi GS4", "Trumpchi GS5", "Trumpchi GS7", "Trumpchi GS8", "Trumpchi M6"
        ]},
        {"Geely": [
            "Arizzo 8", "Atlas", "Atlas Pro", "Azkarra", 'Binary', "Binrui", "Borui GC9",
            "Borui GE", "CE", "CK", "Coolray", "Emgrand", "Emgrand 7", "Emgrand EC7",
            "Emgrand EC8", "Emgrand EV450", "Emgrand EX7/GX7", "Emgrand GL/L", "Emgrand S/GS",
            "eX3", "FC", "FE-1", "GC2", "GC5", "GC6", "Geometry c", "Gleagle GC7", "Gleagle GX7",
            "GS", "GSe", "GX", "Hyra", "LC", "MG", "MK", "MK Cross", "Monjaro", "MR", "Okavango",
            "SC7", "SL", "Smart #1", "STARRAY", "SX 11", 'Tugella', 'UL', "Vision X3/GX3",
            "Vision X6/GX7", "Zeekr 001"
        ]},
        {"General Motors": ["PONTIAC"]},
        {"Genesis": [
            "G70", "G70 Shooting Brake", "G80", "G80 Electrified", "G90", "GTX200", "GV60",
            "GV70", "GV70 Electrified", "GV80"
        ]},
        {"GIO": ["G6"]},
        {"GMC": [
            "Acadia", "Alero", "Canyon", "Envoy", "Hummer EV", "Nummer EV SUV", "Savana",
            "Sierra", "Terrain", "Yukon", "Yukon XL"
        ]},
        {"GPX": [
            "CR5 EFI", "Demon 150 GN", "Demon 150 GR", "Demon GR 200R", "Demon X 125", "Drone",
            "Gentleman 200", "Legend 150", "Legend 200", "Legend 250", "MAD 300", "POPZ 110",
            "ROCK", "Tuscany 150"
        ]},
        {"Great Wall": [
            "C10", "C30", "C50", "Florid", "Haval", 'Haval Dargo', "Haval F5",
            "Haval F7", "Haval F7x", "Haval H1", "Haval H2", "Haval H2s", "Haval H3",
            "Haval H3/Hover", "Haval H5", "Haval H6", "Haval H6 Coupe", "Haval H7",
            "Haval H8", "Haval H9", "Haval Jolion", "Haval M6", "Hover", "M2", "M4",
            "Mustang Yema", "Safe", "SoCool", "Tank 300", "V200", "Voleex C30",
            "Wingle 3", "Wingle 5", "Wingle 6", "Wingle 7", "X200", "X240"
        ]},
        {"Guangzhou Haojin": ["Bike"]},
        {"GWM": [
            "C10", "C20R", "C30", "C50", "Florid X", "Grand Cat", "H5", "Hover", "ORA GOOD CAT",
            "Tank 500", "Voleex C20"
        ]},
        {"H SEM": ["Mobila G", "Mobila S"]},
        {"HAIMA": ["2", "7", "8S", "M3", "S5"]},
        {"Hanway": ["Scrambler"]},
        {"Haojue": ["Haojue UF", "KA", "TR", "TZ"]},
        {"Hartford": ["VR"]},
        {"Haval": [
            "Dargo", "F5", "F7", "F7x", "H1", "H2", "H2s", "H3/Hover", "H5", "H6", "H6 Coupe",
            "H7", "H8", "H9", "Jolion", "M4"
        ]},
        {"HAWTAI": ["B11"]},
        {"Hero": [
            "Achiever", "CBZ", "CD", "Dash", "Dawn 125", 'Duet', 'Glamour',
            "HF", "Hunk", "Karizma", "Maestro", "Passion", "Photon",
            "Pleasure", "Splendor", "Super", "XPulse 200", "XTreme"
        ]},
        {"Hero Honda": [
            "Achiever", 'Glamour', "HF", "Hunk", "Karizma", "Passion", "Splendor", "Super"
        ]},



    ]
    is_agree_with_policy = [("1", "Підтверджую")]
    SMALLEST_SMS_CODE_VALUE = 1000
    HIGHEST_SMS_CODE_VALUE = 9999
    ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
    AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
    AUTH_TOKEN_PHONE_NUMBER = settings.TWILIO_PHONE_NUMBER
