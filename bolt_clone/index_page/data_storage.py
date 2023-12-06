from dataclasses import dataclass

import emoji

from .sort_countries_list import get_select_window_list


@dataclass
class DataStorage:
    NICHE_CHOICE = (
        ("Заклад харчування", "Заклад харчування"),
        ("Продуктовий магазин", "Продуктовий магазин"),
        ("Крамниця", "Крамниця"),
        ("Інший роздрібний магазин", "Інший роздрібний магазин")
    )

    CUISINES_CHOICE = (
        (emoji.emojize(":flag_azerbaijan: Азербайджанська кухня"), "Азербайджанська кухня"),
        (emoji.emojize(":chopsticks: Азійська кузня"), "Азійська кухня"),
        (emoji.emojize(":flag_united_states: Американська кухня"), "Американська кухня"),
        (emoji.emojize(":flag_saudi_arabia: Арабська кухня"), "Арабська кухня"),
        (emoji.emojize(":globe_showing_europe_africa: Африканська кухня"), "Африканська кухня"),
        ("Бабл чай", "Бабл чай"),
        (emoji.emojize(":cookie: Безглютенова"), "Безглютенова"),
        (emoji.emojize(":cheese_wedge: Безлактозна"), "Безлактозна"),
        (emoji.emojize(":camel: Близькосхідна кухня"), "Близькосхідна кухня"),
        (emoji.emojize(":flag_brazil: Бразильська кухня"), "Бразильська кухня"),
        ("Бранч", "Бранч"),
        (emoji.emojize(":hamburger: Бургери"), "Бургери"),
        (emoji.emojize(":flag_vietnam: В'єтнамська кухня"), "В'єтнамська кухня"),
        (emoji.emojize(":dumpling: Вареники"), "Вареники"),
        (emoji.emojize(":broccoli: Веганська кухня"), "Веганська кухня"),
        (emoji.emojize(":green_apple: Вегетеріанська кухня"), "Вегетеріанська кухня"),
        (emoji.emojize(":fork_and_knife_with_plate: Вечеря"), "Вечеря"),
        (emoji.emojize(":cupcake: Випічка"), "Випічка"),
        (emoji.emojize(":flag_armenia: Вірменська кухня"), "Вірменська кухня"),
        (emoji.emojize(":pot_of_food: Вок"), "Вок"),
        (emoji.emojize(":pot_of_food: Вулична їжа"), "Вулична їжа"),
        (emoji.emojize(":flag_ghana: Ганська кухня"), "Ганська кухня"),
        ("Гастро", "Гастро"),
        ("Гірос", "Гірос"),
        (emoji.emojize(":hot_pepper: Гостра"), "Гостра"),
        (emoji.emojize(":flag_greece: Грецька кухня"), "Грецька кухня"),
        (emoji.emojize(":fire: Гриль"), "Гриль"),
        (emoji.emojize(":flag_georgia: Грузинська кухня"), "Грузинська кухня"),
        (emoji.emojize(":fish_cake_with_swirl: Десерт"), "Десерт"),
        ("Для гурманів", "Для гурманів"),
        (emoji.emojize(":squinting_face_with_tongue: Домашня їжа"), "Домашня їжа"),
        (emoji.emojize(":stuffed_flatbread: Донер"), "Донер"),
        (emoji.emojize(":alarm_clock: Електроніка"), "Електроніка"),
        (emoji.emojize(":flag_ethiopia: Ефіопська кухня"), "Ефіопська кухня"),
        (emoji.emojize(":flag_european_union: Європейська кухня"), "Європейська кухня"),
        (emoji.emojize(":avocado: Здорова їжа"), "Здорова їжа"),
        (emoji.emojize(":paw_prints: Зоотовари"), "Зоотовари"),
        (emoji.emojize(":flag_india: Індійська кухня"), "Індійська кухня"),
        (emoji.emojize(":flag_spain: Іспанська кухня"), "Іспанська кухня"),
        (emoji.emojize(":flag_italia: Італійська кухня"), "Італійська кухня"),
        (emoji.emojize(":hot_beverage: Кава"), "Кава")
    )
