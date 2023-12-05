import json


def read_file():
    with open("countries_codes.json", encoding="utf-8") as json_data:
        countries_dict = json.load(json_data)
    return countries_dict


def parse_countries_dict():
    countries_dict = read_file()
    res_list = [countries_dict[country] for country in countries_dict]
    return res_list


def sorted_countries_list():
    countries_list = parse_countries_dict()
    countries_list = sorted(countries_list, key=lambda obj: obj["title"])
    return countries_list



print(sorted_countries_list())
