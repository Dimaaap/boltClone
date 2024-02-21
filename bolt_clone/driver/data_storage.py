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
        {"Aprilia": ["ETX", "RS4", "SR", "STX"]},
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
        {"Exceed": ["LX", "TX", "VX"]},
        {"FAW": [
            "Bestune B30", "Bestune B50", "Bestune B70", "Bestune B90", "Bestune E01", "Bestune T33",
            "Bestune T55", "Bestune T77", "Bestune T99", "Bestune X40", "Bestune X80", "CA 6371",
            "CA 7158", "Diandongwu Young Mini EV", "R7", "S80", "T77", "V2", "V5", "V80", "X40"
        ]},
        {"Fecon": ["Bike"]},
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
        {"Holden": [
            "Acadia", "Astra", "Barina", "Berlina", "Calais", "Caprice", "Captiva", "Clubsport",
            "Colorado", "Commodore", "Cruze", "Epica", "Equinox", "Evoke", "Malibu", "Spark",
            "Statesman", "Trailblazer", "Trax", "Viva", "Volt"
        ]},
        {"Honda": [
            "Accord", "Ace", "Activa", "Acura MDX", "ADV 150", "ADV 160", "ADV 350", "Air Blade",
            "Airwave", "Amaze", "Aria", "Aviator", "Ballade", "Bike", "BR-V", "Brio", "Brio Amaze",
            "Brio Mobilio", "Cargo 150", "CB", "CB 125", "CB 125F Twister", "CB 150R", "CB 190R",
            "CB 250 Twister", "CB 300R", "CB 500X", "CBF", "CBR", "CBR 250R", "CBR 650F", "CBR 650R",
            "CD", "CG", "CGL 125 Tool", "City", "Civic", "Clarity", "Click 110i", "Click 125i",
            "Click 1150i", "Click 160i", "CR-V", "CRF", "Crossroad", "Crosstour", "Cruising 125",
            "CT125", "Dio", "Dio 110", "Dream", "e", "e:NP1", "e:NS1", "e:Ny1", "Edix", "Element",
            "Elevate", "Elite", "Elysion", "Everus VE-1", "FCX Clarity", "Fit", "Fit Aria",
            "Forza 300", "Forza 350", "FR-V", "Freed", "Giorno", "GL 150", "Grazia", "HR-V",
            "Hybrid", "Icon", "Insight", "Inspire", "Invicta CB 160F", "Jade", "Jazz", "Lead 125",
            "Legend", "Life", "Livo", "M-NV Dongfeng", "Mobilio", "Mobilio Spike", "Moove", "MSX 125",
            "N-WGN", "Navi", "Nova Tena", "Odyssey", "Passport", "PCX", "Phantom", "Pilot", "Rebel",
            "Ridgeline", "Scoopy", "Shuttle", "Siming X-NV", "Sonic 125", "Spacy i", "Spike", "Stepwgn",
            "Stream", "Super Cub 110", "Tornado", "Trigger", "Vezel", "Wave 100", "Wave 110",
            "Wave 125i", "Wave 125R", "WR-V", "XR", "XR 150", "XRE 300", "Zoomer X", "ZR-V"
        ]},
        {"Hongqi": ["E-HS9", "H5", "H9", "HS5", "HS7"]},
        {"Hover": ["CUV"]},
        {"Hozon": ["Neta N01", "Neta S", "Neta U", "Neta V"]},
        {"HSV": ["Tracksport"]},
        {"Hummer": ["H2", "H3"]},
        {"Hyundai": [
            "Accent", "Atos", "Avante", "Azera", "Bayon", "Casper", "Centennial", "Creta", "Custo",
            "Elantra", "Entourage", "Eon", "Equus", "Exter", "Galloper", "Genesis", "Getz", "GRAND i10",
            "Grand Santa Fe Maxcruz", "Grand Starex", "Grandeur", "H-1", "H-1 TQ", "H-200", "HB20",
            "HB20S", "HB20X", "i10", "i20", "i30", "i30 Combi", "i40", "i45", "i800", "iMax", "Ioniq",
            "IONIQ 5", "IONIQ 6", "IONIQ 7", "Ioniq Electric", "ix20", "ix35", "ix55", "Kauai", "Kona",
            "Kona EV", "Lafesta", "Matrix", "Nexo", "Palisade", "Santa Cruz", "Santa Fe", "Santro",
            "Santro Plus", "Solaris", "Sonata", "Starex", "Stargazer", "Staria", "Starks", "Terracan",
            "Tiburon", "Trajet", "Tuscon", "Veloster", "Venue", "Veracruz", "Verna", "Xcent", "XG30"
        ]},
        {"Ikco": ["Dena", "Runna", "Samand", "Samand LX", "Soren", "Tara"]},
        {"Infinity": [
            "EX-series", "EX35", "FX-series", "FX35", "FX37", "G-series", "G25", "G35", "G37", "I30",
            "JX-series", "JX35", "M", "M-series", "Q30", "Q30s", "Q40", "Q45", "Q50", "Q70", "QX30",
            "QX40", "QX50", "QX55", "QX56", "QX60", "QX70", "QX80"
        ]},
        {"Ingrace": ["Estel"]},
        {"Innoson": ["IVM FOX"]},
        {"Iran Khodro": ["Runna", "Soren"]},
        {"ISLO": ["KANGUR", "MUTANT", "RABBIT", "RACER", "RUSH", "SIOUX"]},
        {"Isuzu": ["Ascender", "Axiom", "D-Max", "Gemini", "Isuzu Axiom", "MU-7", "MU-X", "Rodeo"]},
        {"ITALIKA": [
            "125 Z", "150 SZ", "150 Z", "200 Z", "250 Z", "AT 110", "AT 110 RT", "AT 125", "AT 125 RT",
            "D 125", "D 150", "DM 125", "DM 150", "DM 200", "DM 250", "DS 125", "DS 150", "DS 150 G",
            "DSG 125", "DT 110", "DT 125", "DT 150", "DT 200", "DT 250", "FIERA 150", "FT 115", "FT 125",
            "FT 150", "FT 150 GTS", "FT 150 TS", "FT 180 TS", "FT 200 TS", "FT 250 TS", "MODENA 150",
            "MODENA 175", "RC 125", "RC 150", "RC 200", "RT 200", "RT 250", "SPT FIRE 200", "TC 200",
            "TC 250", "V 200", "VITALIA 125", "VITALIA 150", "VORT-X 200", "VORT-X 650", "VORT-X 300",
            "VX 250 EFI", "W 150", "WS 175", "X 125", "X 150", "XS 150", "XT 110", "XT 125 RT", "XW150"
        ]},
        {"Iveco": ["Daily"]},
        {"IZUKA": [
            "CITI 150", "CL 150", "CL 250", "DPL 200", "IZ 180 R", "IZ 250", "KL 125", "KPR 200",
            "TL 125 A", "TL 150 N"
        ]},
        {"JAC Motors": [
            "iEV7s", "iEVS4", "J2", "J3", "J4", "J5", "J6", "J7", "JAC", "JS2", "JS3", "JS8", "S4"
        ]},
        {"Jaguar": [
            "E-Pace", "F-Pace", "F-Pace R-Sport", "I-Pace", "S-Type", "XE", "XF", "XJ", "XJL", "XJR"
        ]},
        {"Jamuna": ["Pegasus"]},
        {"Jeep": [
            "Avenger", "Cherokee", "Cherokee Trailhawk", "Commander", "Compass", "Gladiator",
            "Grand Cherokee", "Grand Wagoneer", "Liberty", "Meridian", "Patriot", "Renegade",
            "Wagoneer", "Wrangler"
        ]},
        {"Jetour": ["Dashing", "X70", "X90"]},
        {"Jiagi": ["S"]},
        {"Jinbei": ["sy1028"]},
        {"Jincheng": ["Baby Machine"]},
        {"JMC": ["Landwind X2"]},
        {"Kantanka": ["Amoanimaa"]},
        {"KAWASAKI": [
            "KLR 650", "KLX 110", "KLX 140", "KLX 230", "KLX 300 R", "KLX 140", "Ninja 400", "Ninja 650",
            "Ninja H2", "Ninja H2R", "Ninja ZX-10R", "Ninja ZX-6R", "Versys 1000", "Versys 650", "Versys X300",
            "Vulcan 1700", "Vulcan 900", "W 175 SE", "Z 900 RS"
        ]},
        {"KEEWAY": [
            "GT270", "K-LIGHT 202", "Magnet", "PATAGONIAN EAGLE 250", "RKR", "RKS", "RKV", "Superlight",
            "SUPERLIGHT 200"
        ]},
        {"Kenton": [
            "Blitz 110", "BLITZ 125", "Bull 200", "Bull 250", "c110", "Cafe Racer 150", "Classic 150",
            "Dakar 150", "Dakar 200", "Forza 150", "Fusion 125", "GL 125", "GL 200", "GL 150",
            "GLX 150", "GTR 150 DLX", "GTR 200", "GTS 150", "Milestone", "Rider 200", "Shark 150",
            "Shark 200", "SKUA 150", "Viva 100"
        ]},
        {"Khazar": ["D5", "LD", "LX", "SD"]},
        {"Kia": [
            "Avella", "Cadenza", "Carens", "Carnival", "Cee`d", "Cee`s Sportswagon", "Ceed",
            "Cerato", "Clarus", "e-Niro", "e-Soul", "EV3", "EV4", "EV5", "EV6", "EV6 GT",
            "EV9", "Forte", "Forte LX", "Joice", "K3", "K5", "K7", "K8", "K9 / K900",
            "Lotze", "Magentis", "Mohave", "Morning", "Niro", "Opirus", "Optima",
            "Pegas", "Picanto", "Pregio", "Pride", "ProCee`d", "Quoris", "Ray", "Rio", "Rio Cross",
            "Rio X Line", "Rio-YB", "Rondo", "Sedona", "Seltos", "Sephia", "Shuma", "Soluto Xcite",
            "Sonet", "Sorento", "Soul", "Soul EV", "Spectra", "Sportage", "Stinger", "Stonic",
            "Telluride", "Venga", "Visto", "XCeed"
        ]},
        {"Kinetic": ["HIRHEV", "Velocity"]},
        {"KTM": [
            "125 Duke", "125 SX", "150 SX", "250 SX", "250 SX-F", "350 SX-F", "390 Duke", "450 SX-F",
            "Duke", "RC", "RC200"
        ]},
        {"KYMCO": ["TOP BOY 125", "X TOWN 250i", "XCITING S 400"]},
        {"Kymstone": ["Husky 200"]},
        {"Lada": [
            "2104 Жигули", "2106 Жигули", "2107 Жигули", "2109 Самара", "21099 Самара", "2110", "2111", "2112",
            "2114 Самара II", "2115 Самара II", "2120 Надежда", "2123 Нива", "2170 Priora", "Granta",
            "Kalina", "Largus", "Niva", "Priora", "Vesta", "XRAY"
        ]},
        {"Lamborghini": ["Aventador", "Gallardo", "Huracan", "Revuelto", "Sterrato", "Urus"]},
        {"Lambretta": ["V125", "V200", "V300"]},
        {"Lancia": ["Delta", "LX", "Lybra", "Musa", "Phedra", "Thema", "Thesis", "Voyager", "Ypsilon"]},
        {"Land Rover": [
            "Defender", "Discovery", "Discovery Sport", "Evoque", "Freelander"
        ]},
        {"LDV": ["G10", "Maxus", "T60"]},
        {"Leapmotor": ["C11", "T03"]},
        {"Leopard": [
            "EN125 - YES", "EN150", "EN150 Sport", "EN200", "GSX150", "GTS150STD", "HB110 buzz",
            "HT 150", "HT 200", "KH 150", "KH 180", "MD 125", "MD 150", "MD200 TC", "MT -150",
            "MT -25", "STREET 15-", "STREET 200"
        ]},
        {"LEVC": ["LEVC TX VISTA COMFORT", "LEVC TX VISTA COMFORT PLUS", "LEVC TXE", "TX", "TX Vista"]},
        {"Lexus": [
            "BYD F6", "CT", "CT200h", "ES", "ES250", "ES300", "ES300h", "ES330", "ES350", "GS", "GS200t",
            "GS300", "GS300h", "GS450h", "GX", "HS", "IS", "IS 300h", "LBX", "LS", "LX", "LX570", "NX",
            "NX300", "NX300h", "NX450h", "NX450H+", "RX", "RX400H", "RX450H", "RX450h", "RX450hL",
            "RZ", "TX", "UX", "UX F-Sport", 'UX200', "UX250h", "UX300e"
        ]},
        {"Lifan": [
            "214835", "320", "520", "620", "720", "820", "AR 125", "Bike", "Cebrium", "FR 200", "Glint",
            "GY 200", "KP", "KP mini 150", "KP150", "KPR", "KPR 200", "KPS", "KPT", "LF 110",
            "LF 6420", "LF 7160", "Maple", "Meiwei", "Myway", "NAZ", "NAZ LF 720"
        ]},
        {"Lincoln": [
            "Aviator", "Continental", "Corsair", "LS", "MKC", "MKS", "MKT", "MKX", "MKZ", "Nautilus",
            "Navigator", "Town Car"
        ]},
        {"Link Tour": ["EV"]},
        {"LML": ["STAR 125", "STAR 200", "STAR 4T 125", "STAR 4T 200"]},
        {"London Cab": ["TX4", "TX5"]},
        {"Lotus": ["Eletra", "Emeya", "Envya", "Evija"]},
        {"Lynk&Co": ["01", "02", "03", "05", "06", "07", "09"]},
        {"Mahindra": [
            "4x4", "Alfa (TukTuk)", "Arro", "Bike", "Centuro", "Duro", "Flyte", "Gusto", "KUV 100",
            "Pantero", "Rodeo", "TUV 300", "XUV 300", "XUV 500", "XYLO SUV"
        ]},
        {"Malaguti": ["Madison 150"]},
        {"Mana": ["E-Bike"]},
        {"Maruti": [
            "HB110 Buzz", "KN 250 GS", "KORAK 110", "MD-150", "MT-125", "MT-150", "MT-200", "PHANTOM300",
            "PLUS 150 CC", "TUK 200"
        ]},
        {"Maserati": [
            "Ghibli", "GranTurismo", "GranTurismo Folgore", "Grecale", "Grecale Folgore", "Levante",
            "Quattroporte"
        ]},
        {"Maxus": ["D60", "Euniq 5", "Euniq 6", "EV30"]},
        {"Maybach": [
            "57", "57 Zeppelin", "57s", "62", "62 Landaulet", "62 Zeppelin", "62s", "G 650 Landaulet",
            "GLS 600", "S-class"
        ]},
        {"Mazda": [
            "2", "3", "300", "323F", "5", "6", "626", "Allegro", "Atenza", "Axela", "AZ", "Biante",
            "BT-50", "Capella", "Carol", "CX", "CX-3", "CX-30", "CX-4", "CX-5", "CX-50", "CX-60",
            "CX-7", "CX-8", "CX-9", "CX-90", "Demio", "Familia", "Flair", "Millenia", "MPV", "MX-30",
            "Premacy", "Protege", "RX-8", "Tribute", "Verisa", "Versia", "Xedos 6", "Xedos 9"
        ]},
        {"McLaren Automotive": ["P650"]},
        {"Mercedes-Benz": [
            "190", "200", "200c", "270", "A-class", "A170", "A180", "A200", "A250", "AMG GT 4-Door Coupe",
            "B-class", "B180", "B200", "B220", "B250", "C-class", "C180", 'C200', "C220", "C240", "C250",
            "C270", "C300", "C320", "C350", "CBT", "Citan", "CLA", "CLA Shooting Brake", "CLA200", "CLA220",
            "CLK", "CLS", "CLS220", "CLS250", "E320", "E-class", "E-class Limousine", "E200", "E220",
            "E250", "E300", "E350", "E400", "E53 AMG", "EQA", "EQB", "EQC", "EQC 400", "EQE", "EQE SUV",
            "EQS", "EQS SUV", "EQT", "EQV", "EQV 300", "eVito", "G-class", "G63 AMG", "GL", "GLA", "GLA200",
            "GLA220", "GLB", "GLC", "GLC Coupe", "GLC200", "GLC220", "GLC250", "GLC250d", "GLC350e", "GLE",
            "GLE Coupe", "GLE350", "GLS63", "M-class", "ML-class", "ML250", "ML350", "R-class", "R350",
            "S-class", "S300", "S350", "S400", "S450", "S500", "S560", "S580", "S65 AMG", "S650", "SL",
            "Sprinter", "T 180 D", "V-class", "V220", "V250", "V300", "Valente", "Vaneo", "Viano", "Vito",
            "Vito 113", "Vito 114", "Vito 116", "Vito 119", "Vito 220", "VITO TAXI", "VITO VAXI+", "X-class"
        ]},
        {"Mercury": ["Mariner", "Milan", "Mountaineer"]},
        {"MG": [
            "-", "3", "350", "4 EV", "5", "5 EV", "550", "6", "750", "Cyberster", "EP", "ES", "Extender",
            "F3", "GS", "GT", "HS", "Jeely Rand", "M5", "Marvel R", "Marvel X", "MG eHS", "MG4", "MG5",
            "One a", "One B", "RX5", "RX8", "V80", "VS HEV", "ZS", "ZS EV"
        ]},
        {"Micro": ["MPV Junior 3"]},
        {"MINI": ["Aceman", "Clubman", "Cooper", "Countryman", "Paceman"]},
        {"Mitsubishi": [
            "Airtrek", "ASX", "Attrage", "Carisma", "Challenger", "Chariot",
            "Colt", "Colt Plus", "Delica", "Eclipse", "Eclipse Cross", "EK", "Endeavor", "Galant",
            "Grandis", "i-MiEV", "L200", "Lancer", "Lancer Evolution", "Mirage", "Montero",
            "Outlander", "Outlander Sport", "Pajero", "Pajero iO", "Pajero Sport", "RVR", "Shogun",
            "Space Star", "Space Wagon", "Triton", "XFC", "Xforce", "Xpander", "Xpander Cross", "Xpander GT"
        ]},
        {"MOTO GUZZI": ["AUDACE CARBON", "V 85 TT", "V7 II RACER", "V7 III STONE", "B9 BOBBER", "V9 ROAMER"]},
        {"Motostar": [
            "SK 110 DAX-A", "SK 125-5", "SK 150-NT-A", "SK BR200", "SK150-BR-New", "SK150-X-CKD", "SMX150",
            "Star 200", "XPRO 150", "XPRO 200"
        ]},
        {"MPM motors": ["Erelis"]},
        {"MV AGUSTA": ["BRUTALE 1090", "BRUTALE 675", "BRUTALE 800", "F3 675", "F4 RR", "RIVALE 800"]},
        {"Neta": ["U Pro 400", "V", "V Chao 400 Lite", "X"]},
        {"Nio": ["EC6", "EC7", "EL7", "ES7", "ES8", "ET5", "ET5 Orion", "ET7"]},
        {"Nissan": [
            "AD", "Advan", "Almera", "Almera Classic", "Altima", "Aprio", "Ariya", "Armada", "Bluebird",
            "Caravan", "Cedric", "Cefiro", "Cube", "Dayz", "Dualis", "Dualis 2", "e-NV200 Dynamo",
            "Elgrand", "Frontier", "Fuga", "Gloria", "GT-R", "Juke", "Kicks", "Kubistar", "Lafesta",
            "Latio", "Leaf", "Liberty", "Livina", "Magnite", "March", "Maxima", "Maxima QX",
            "Micra", "Mocco", "Murano", "Navara", "Note", "NV100 Clipper", "NV200", "NV300",
            "NV350", "NV400", "Otti", "Pathfinder", "Patrol", "Pino", "Pintara", "Pixo",
            "Platina", "Presage", "Presea", "Primastar", "Primera", "Pulsar", "Qashqai", "Qashqai+2",
            "Quest", "Rogue", "Sentra", "Serena", "Skyline", "Sunny", "Sylphy", "Teana", "Terra", "Terrano",
            "Tiida", "Titan", "Townstar", "Tsuru", "V-Drive", "Versa", "Wingroad", "X-Tera", "X-Trail"
        ]},
        {"NIU": ["NQi"]},
        {"Opel": [
            "Adam", "Agila", "Ampera", "Ampera-e", "Antara", "Astra", "Astra Classic", "Astra Sports Tourer",
            "Cascada", "Combo Life", "Combo Tour", "Combo-e Life", "Corsa", "Corsa-e", "Crossland X", "Frontera",
            "Grandland X", "Insignia", "Karl", "Meriva", "Mokka", "Mokka-e", "Mavano", "Omega", "Signum",
            "Sintra", "Vectra", "Vectra C", "Vita", "Vivaro", "Vivaro-e", "Zafira", "Zafira-e"
        ]},
        {"Paggio": [
            "CT100", "Elegante", "LT", "LX", "SXL", "V12", "V15", "VXL"
        ]},
        {"Perodua": ["Alza", "Aruz", "Axia", "Bezza", "Myvi"]},
        {"Peugeot": [
            "107", "108", "2008", "206", "206+", "207", "207 SW", "208", "3008", "301",
            "306", "307", "307 SW", "308", "308 SW", "4007", "4008", "405", "406", "407",
            "407 SW", "408", "5008", "508", "508 SW", "607", "806", "807", "Bipper", "Boxer",
            "Boxer 335", "Boxer 436", "Django", "e-2008", "e-208", "e-Rifter", "e-Traveller",
            "Expert", "Expert Combi", "Expert Eurobus", "Expert G9", "Expert Independence",
            "Expert Tepee", "Horizon", "iOn", "Pars", "Partner", "Pragya", "Premier", "Rifter", "Traveller"
        ]},
        {"PHP": ["Merkaba", "Pride"]},
        {"Piaggio": ["Rickshaw (TukTuk)"]},
        {"Plymouth": ["Neon"]},
        {"Polestar": ["1", "2", "3", "4"]},
        {"Pontiac": ["G3", "G6", "G8", "Grand Prix", "Torrent", "Vibe", "Wave"]},
        {"Porsche": [
            "911", "Boxter", "Cayenne", "Cayenne Coupe", "Cayman", "Macan", "Panamera", "Panamera Sport Turismo",
            "Taycan", "Taycan Cross Turismo", "Taycan Sport Turismo"
        ]},
        {"Pragya": ["Bajaj", "CVS", "Qute"]},
        {"Proton": ["BT3SRSRM4A", "EXORA", "GEN2", "Persona", "Preve", "Saga", "Savvy"]},
        {"Quantum Technologies": ["E4"]},
        {"Qute": ["Pragya"]},
        {"Race": ["City", "Fiero", "Hyosung", "SR"]},
        {"Range Rover": ["Evoque", "Sport", "Velar", "Vogue"]},
        {"Ravon": ["Gentra", "Nexia", "R2", "R3", "R4"]},
        {"Regal": ["Prince Pearl"]},
        {"Renault": [
            "19", "Alaskan", "Arkana", "Austral", "Avantime", "Captur", "City K-ZE", "Clio",
            "Clio Estate", "Clio Grandtour", "Clio Symbol", "Dokker", "Duster", "Espace",
            "Express", "Fluence", "Fluence Z.E.", "Grand Espace", "Grand Modus", "Grand Scenic",
            "Kadjar", "Kangoo", "Kangoo Z.E.", "Kaptur", "Karian", "Kiger", "Koleos", "Kwid", "Laguna",
            "Latitude", "Lodgy", "Logan", "Logan II", "Logan MCV", "Master", "Megane", "Megane E-Tech Electric",
            "Megane Grandcoupe", "Megane Grandtour", "Megane Scenic", "Modus", "Orosh", "Rafale", "Safrane",
            "Samsung", "Sandero", "Scala", "Scenic", "Stepway", "Symbol", "Talisman", "Talismane Berline",
            "Thalia", "Tondar", "Trafic", "Triber", "Twingo", "Vel Satis", "Zoe"
        ]},
        {"Renault Samsung": [
            "QM3", "QM6", "SM3", "SM3 Z.E.", "SM5", "SM6", "SM7", "XM3"
        ]},
        {"Rio": ["Taxi"]},
        {"Road Prince": ["Classic", "Jackpot", "Passion", "Power +", "ROBINSON", "RX3", "Shift 125", "WEGO"]},
        {"Roadmaster": ["Delight", "Prime", "Rapido", "Rex", "Velocity"]},
        {"Rolls-Royce": [
            "Cullinan", "Dawn", "Ghost", "Phantom Coupe", "Phantom Drophead Coupe", "Phantom VII", "Spectre",
            "Wraith"
        ]},
        {"Rongxing": ["RX200"]},
        {"Rover": ["25", "416 GSI", "45", "75", "MG ZT", "Sport", "Streetwise"]},
        {"Royal Alloy": ["GP 150"]},
        {"Royal Enfield": ["Bullet", "Classic", "Continental", "Himalayan", "Interceptor", "ThunderBird"]},
        {"Runner": [
            "AD80S", "Bike", "Bullet", "Cheeta", "Deluxe", "F100", "Kite", "KnightRider", "Royal", "Turbo", "UM"
        ]},
        {"Saab": ["9-3", "9-4X", "9-5", "9-7X"]},
        {"SABA": ["GLXI", "Scooter"]},
        {"Saic": [
            "Maxus D60", "Maxus D60e", "Maxus D90", "Maxus Euniq 6", "Maxus Euniq 6 Grand SUV",
            "Maxus Euniq 9", "Roewe 360", "Roewe 950", "Roewe Ei5", "Roewe i5", "Roewe i6", "Roewe Marvel R",
            "Roewe Marvel X", "Roewe RX3", "Roewe RX5", "Roewe RX5 Max"
        ]},
        {"Saipa": ["131", "132SE", "Quick", "Saina", "SX", "Tiba"]},
        {"Salti": ["S200"]},
        {"Samand": ["AZ", "AZ Runna", "CNG", "Dena", "EL", "Ikco", "LX", "SE", "Soren"]},
        {"SanLG": ["Bike"]},
        {"Saturn": ["Astra", "Aura", "Ion", "Outlook", "Vue"]},
        {"Scion": ["iA", "iM", 'tC', "xA", "xB", "xD"]},
        {"Scomadi": ["tt 125i"]},
        {"Seat": [
            "Alhambra", "Altea", "Altea XL", "Arona", "Ateca", "Cordoba", "Exeo", "Ibiza", "Leon",
            "Leon Estate", "Mii", "Tarraco", "Toledo"
        ]},
        {"Senova": ["A1", "Baic"]},
        {"Seres": ["3", "E3"]},
        {"Shangai": ["Englon", "Maple", "SCEO"]},
        {"Shineray": ["MPV750"]},
        {"Siytto": ["SVI-150"]},
        {"Skoda": [
            "Citigo", "Enyaq", "Enyaq iV", 'Fabia', "Fabia Combi", "Felicia", "Kamiq", "Karoq", "Kodiaq",
            "Kushaq", "Octavia", "Octavia Estate", "Praktik", "Rapid", "Rapid Spaceback", "Roomster",
            "Scala", "Slavia", "Superb", "Yeti"
        ]},
        {"Skywell": ["EV6"]},
        {"SMART": ["#1", "EQ ForFour", "ForFour", "ForTwo"]},
        {"Sonlink": ["SL125"]},
        {"Soueast": ["A5 Yiwu", "DX3", "DX5", "DX7", "DX9", "Lioncel"]},
        {"Speranza": ["A516", "Envy"]},
        {"SsangYong": [
            "Actyon", "Korando", "Kyron", "Rexton", "Rodius", "Stavic", "Tivoli", "Turismo", "XLV Estate"
        ]},
        {"Star": ["Desert TR5", "SK 150-NT-A", "SK200 - DESERT", "SMX150", "TRC-150CC", "XPRO150-R", "XPRO200-R"]},
        {"Strom": ["Chimpanzee", "GORILLA", "LEOPARD", "PANTHER", "SEA-100L"]},
        {"Subaru": [
            "Ascent", "Crosstrek", "Forester", "Impreza", "Impreza WRX STI", "Justy", "Legacy", "Levorg",
            "Liberty", "Outback", "Pleo", "Solterra", "Stella", "Traviq", "Trezia", "Tribeca", "Vivio",
            "WRX", "XV"
        ]},
        {"Suda": ["SA01"]},
        {"Suzuki": [
            "Access", "Across", "Aerio", "Alto", "AN125", "APV", "AX 100", "AX 4", "Baleno", "Best 110",
            "Best 125", "BRGMAN", "BURGMAN STREET", "C 50", "Celerio", "Cervo", "Ciaz", "Cultus VXL",
            "Cultus VXR", "Dzire", "EN 125 - 2A", "Ertiga", "Escudo", "Every", "FD 110", "Forenza",
            "Forenzai", "GF 110", "GF", "Gixxer", "GIXXER SF 250", "GN 125 F", "GN125", "GR 650",
            "Grand Vitara", "GS150R", "GSX - S150", "GSX S750", "GSX-R 1000 A", "GSX-R 1000 R",
            "GSX-R 150", "GSX-R 600", "GSX-R 750", "GZ150", "HAYABUSA", "Hayate", "HURACAN", "Hustler",
            "Ignis", "Intruder", "Jimny", "KATANA", "Kei", "Khyber", "Kizashi", "Landy", "Let`s", "Liana",
            "M 109 R", "Mehran", "Palette", "Raider R150 Fi", "Reno", "S 40", "S-Presso", "Shooter",
            "Skydrive", "Slingshot", "Smash", "Solio", "Spacia", "Splash", "Step 125", "Suzuki Crevo", "Swace",
            "Swift", "Swish", "SX4", "SX4 S-Cross", "Thunder", "V-STROM 1000", "V-STROM 250", "V-STROM 650",
            "V-STROM 650 XT", "Verona", "Vitara", "VSTROM 1000 XT", "Wagon", "Wagon R", "XL-7"
        ]},
        {"Sym": ["GR"]},
        {"T better": ["Better"]},
        {"Taiga": ["TL 125-5", "TL 150 CR1", "TL 200 GY-3B", "TL 200 SUPERLIGHT", "TL 250 CR5", "TL110-2GF"]},
        {"TAILG": ["TL1500"]},
        {"Tata": [
            "Aria", "Bolt", "Indica", "Indigo", "Nano", "Nexon", "Safari Storme", "Tiago", "Tigor", "Vista",
            "Xenon", "Zest"
        ]},
        {"Tesla": ["Cybertruck", "Model 3", "Model S", "Model X", "Model Y"]},
        {"Test Model": ["Tuk-tuk"]},
        {"Tobe": ["M`Car"]},
        {"Toyota": [
            "100", "110", "4Runner", "Aerio", "Agya", "Allex", "Allion", "Alphard", "Altezza", "Altis",
            "Aqua", "Aristo", "Ateva", "Aurion", "Auris", "Avalon", "Avanza", "Avensis", "Avensis Verso",
            "Axio", "Aygo", "Aygo X", "BB", "Belta", "Blade", "Brevis", "bZ4X", "C-HR", "C-RV", "Caldina",
            "Cami", "Camry", "Carib", "Carina", "Cavalier", "CBA-ZNE10G", "Century", "Chaser", "Coaster",
            "Commuter", "Corolla", "Corolla Cros", "Corolla Touring", "Corolla Verso", "Corona", "Corsa",
            "Cosra", 'Cresta', "Cross", "Crown", "Daihatsu", "Duet", "Echo", "Esquire", "Estima", "Etios",
            "Fiedler", "FJ Cruiser", "Fortuner", "Funcargo", "G-Touring", "Gaia", "Grand Hiace", "Grand Highlander",
            "GX-R", "Harrier", "HiAce", "Highlander", "Hilux", "Hilux Revo", "Hilux Vigo", "Innova", "Ipsum",
            "IQ", "Isis", "Ist", "Kaluga", "Kigege", "Kluger", "Land Cruiser", "Land Cruiser VXR",
            "La Prado", "Mark II", "Mark X", "Matrix", "Mirai", "Nadia", "Noah", "NZE", "Opa", "Passo",
            "Passo Sette", "Picnic", "Pixis", "Platz", "Porte", "Premio", "Previa", "Prius", "Prius Plus",
            "Prius v", "Prius c", "ProAce", "ProAce City Verso", "ProAce Verso", "Probox", "Progress",
            "Quantum", "Ractis", "Raum", "RAV4", "Reguis", "Reiz", "Ruckus", "Rumion", "Runx", "Rush 800", "SAI",
            "Scion", "Sequoia", "Sienna", "Sienta", "Solara", "Soluna", "Spacio", "Spade", "Sprinter",
            "Starlet", "Succeed", "Tacoma", "Tarago", "Tercel", "Toyota Allion", "Tundra", "Urban Cruiser",
            "Vellfire", "Veloz", "Ventury", "Venza", "Verossa", "Verso", "Verso S", "Vios", "Vista", "Vitz",
            "Voltz", "Voxy", "Will", "Windom", "Wish", "xA", "Yaris", "Yaris Ativ", "Yaris Cross", "Yaris Verso"
        ]},
        {"Tris": ["Concode", "Concode 139"]},
        {"TRIUMPH": [
            "BONNEVILE", "ROCKET 3", "SCRAMBLER 1200", "SPEED TWIN", "STREET TRIPLE", "THRUXTON", "TIGER 1200",
            "TIGER 660", "TIGER 800", "TIGER 900"
        ]},
        {"Trumpchi": ["GA3"]},
        {"TVS": [
            "Apache", "Apache 160", "Apache RR310", "Apache RTR 160", "Apache RTR 180", "Apache 200",
            "Bike", "Classic", "Dazz", "HX150", "Jupiter", "King (TukTuk)", "Metro", "NTORQ 125",
            "Phonix", "Raider", "ROCKZ 125", "Scooty", "Scrambler", "Star", "Star HLX-150", "Star HLX-100",
            "Stryker", "Stryker 125", "TVS 100", "Victor", "Wego"
        ]},
        {"Twinco": ["Eagle"]},
        {"Um": ["DSR", "ETX", "Hypersport", "Nitrox", "PowerMax", "Renegade", "RS4", "SR", "STX", "Xtreet"]},
        {"United": ["Alpha", "Bravo"]},
        {"Vauxhall": [
            "Adam", "Agila", "Ampera", "Ampera-e", "Antara", "Astra", "Cascada", "Combo", "Combo Life",
            "Combo Tour", "Corsa", "Corsa-e", "Crossland", "Crossland X", "Grandland", "Grandland X",
            "Insignia", "Meriva", 'Mokka', "Mokka-e", "Movano", "Signum", "Vectra", "Vivaro", "Vivaro-e",
            "Z", "Zafira", "ZS", "ZS80"
        ]},
        {"Vector": ["150"]},
        {"Vento": [
            "302", "Atom 150", "Crossmax 200", "Crossmax 250", "Cyclone 150", "Cyclone 200", "Hotrod 150",
            "Leoncino", "Lithium 150", "Lucky 7 400", "Nitrox 200", "Nitrox 250", "Phantom 150 ZX", "Rocketman 250",
            "Ryder 150", "Spectra 5i", "Terra ROD 150", "Thriller 200", "Thunderstar 250", "TNT", "Tornado",
            "Tornado 250", "Workman 150", "Workman 250"
        ]},
        {"VESPA": ["GTS", "LX 125", "Primavera", "PX", "S 125", 'Sprint', 'Xz450']},
        {"VGV": ["U70 PRO", "U75 PRO"]},
        {"Victor-R": ["110", "Classic", 'Deviser', "DY100", "Plight", "Roebuck", "Sprout", "V100", "V80"]},
        {"Volga": ["3110", "31105", "3111", "Gaz 24", "KA", "Siber", "TR", "TZ"]},
        {"Volkswagen": [
            "Amarok", "Arteon", "Arteon Shooting Brake", "Atlas", "Beetle", "Bora", "Caddy", "Caddy Inva",
            "Caddy Maxi", "California", "Caravelle", "CC", "Crafter", "CrossFox", "e-Bora", "e-Golf", "e-Lavida",
            "e-Up", "Eos Cabrio", "Fox", "Gol", "Gol Sedan / Voyage", "Golf", "Golf GTE", "Golf GTI",
            "Golf Plus", "Golf Sportsvan", "Golf Variant", "ID.3", "ID.4", "ID.5", "ID.6", "ID.6 Crozz",
            "ID.7", "ID.Buzz", "Jetta", "Jetta Clasico", "Jetta Europa A4", "Koi", "Kombi", "LT35",
            "Lupo", "Multivan", "Nivus", "Parati Surf", "Passat", "Passat CC", "Passat Combi", "Phaeton",
            "Phideon", "Pointer", "Polo", "Polo Sedan", "Polo Vivo", "Routan", "Scirocco", "Sharan", "Shuttle",
            "Suran", "T-Cross", "T-Roc", "Taigo", "Taos", "Teramont", "Tharu", "Tiguan", "Touareg", "Touran",
            "Transporter", "Transporter California", "Transporter Caravan", "Transporter Caravelle",
            "Transporter Kombi", "Transporter Multivan", "Up", "Vento", "Virtus", "Voyage", "VR"
        ]},
        {"Volvo": [
            "Achiever", "C30", "C40 Recharge", "C70", 'CBZ', "CD", "Dash", "Duet", "EX30", "EX90",
            "Glamour", "HF", "Hunk", "Karizma", "Maestro", "Passion", "Photon", "Pleasure", "S40",
            "S60", "S70", "S80", "S90", "Splendor", "Super", "V40", "V40 Cross Country", "V50",
            "V60", "V60 Cross Country", "V70", "V90", "V90 Cross Country", "XC40", "XC40 Recharge",
            "XC60", "XC70", "XC90", "Xtreme"
        ]},
        {"Vortex": [
            "Achiever", "Estina", "Glamour", "HF", "Hunk", "Karizma", "Passion", "Splendor", "Super",
            "Tingo", "Xtreme"
        ]},
        {"Walton": [
            "Cruize", "Fusion", "Leo", "Prizm", "Ranger", "Stylex", "Xplore"
        ]},
        {"Weltmeister": ["E5", "EX5", "EX5 Pro", "EX5-Z", "EX6", "EX6 Plus 6", "W6"]},
        {"Winnonie": ["Winnonie"]},
        {"Wuling Motors": ["Bingo"]},
        {"Xpeng": ["G3", "G3i", 'G9', "P5", "P7"]},
        {"Yamaha": [
            "Aerox", 'AG200', "Alpha", "BW`s 125", "Crux", "Cygnus Alpha", "Cygnus ZR", "Enticer", "Exciter 150",
            "Fascino", "Fazer", "Fazer FI 2", "Fazzio", "Finn", "Fino","Fino 125", "Fiore", "FreeGo", "FZ",
            "FZ 25", "FZ FI", "FZ-S FI", "FZS", "Gladiator", "Grand Filano", "GT 125", "Jupiter RC", "Lexi",
            "M", 'M-Slaz', 'Mio 115', "Mio 125", "Mio Fazzio", "Mio Fino FI", "MT-03", "MT-07", "MT-09",
            "MT-125", "MT-15", "NMAX", 'Nouvo E', "Nouvo MX", "Nouvo SX", "QBIX", "R15", "Ray", "Ray zr",
            "Saluto", "Spark 115i", "Spark 135", "Speed", "SR400", "SS", "SZ", "SZ-RR", "T110 Crypton",
            "Tenere 250", "Tricity 155", "TTX", "WR155R", "XMAX 300", "XSR 125", "XSR 155", "XSR 900",
            "XT 1200 Z", "XTZ 125 E", "XTZ 150", "XVS 250 VSTAR", "SVS 950 BOLT", "YB 125", "YBR", "YBR 125 C",
            "YBR 125 ZR", "YBR 125G", "YC-Z 110", "YS125", 'YZF', "YZF-R1" ,"YZF-R15", 'YZF-R3' ,"YZF-R6"
        ]},
        {"Yamazuki": ["F 125 AZ", "GX 200"]},
        {"ZAZ": ["Forza", "Lanos", "Sens", "Vida"]},
        {"Zeekr": ["001", "007", "009", "X"]},
        {"Zongshen": ["CG-125", "Ruyka Classic", "Ruyka Classic R Fi", "Ruyka RK250", "Spark", "ZS"]},
        {"Zotye": ["Coupa", "Nomad 1.3", "T600", "Z100", "Z300"]}
    ]
    CAR_CREATED_YEAR_LIST = [(str(i), (str(i))) for i in range(2000, 2026)]
    CAR_COLORS_LIST = [
        ("Білий", "Білий"),
        ("Чорний", "Чорний"),
        ("Синій", "Синій"),
        ("Зелений", "Зелений"),
        ("Жовтий", "Жовтий"),
        ("Червоний", "Червоний"),
        ("Фіолетовий", "Фіолетовий"),
        ("Сірий", "Сірий"),
        ("Коричневий", "Коричневий"),
        ("Бежевий", "Бежевий"),
        ("Рожевий", "Рожевий"),
        ("Помаранчевий", "Помаранчевий"),
        ("Золотий", "Золотий"),
        ("Сріблястий", "Сріблястий"),
        ("Бронзовий", "Бронзовий"),
        ("Бордовий", "Бордовий"),
        ("Винний", "Винний"),
        ("Винний червоний", "Винний червоний"),
        ("Небесно-блакитний", "Небесно-блакитний"),
        ("Небесно-блакитний", "Небесно-блакитний"),
        ("Блакитний", "Блакитний"),
        ("Перламутрово білий", "Перламутрово білий"),
        ("Перламутровий", "Перламутровий"),
        ("Темно-сірий", "Темно-сірий"),
        ("Темно-синій", "Темно-синій"),
    ]
    is_agree_with_policy = [("1", "Підтверджую")]
    SMALLEST_SMS_CODE_VALUE = 1000
    HIGHEST_SMS_CODE_VALUE = 9999
    ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
    AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
    AUTH_TOKEN_PHONE_NUMBER = settings.TWILIO_PHONE_NUMBER
