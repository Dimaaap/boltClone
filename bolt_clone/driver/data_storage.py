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
    is_agree_with_policy = [("1", "Підтверджую")]