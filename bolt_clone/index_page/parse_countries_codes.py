import requests
import json

URL = "https://restcountries.com/v3.1/all"


def get_country_codes():
    try:
        response = requests.get(URL)
        countries_json = response.json()
        country_phone_codes = {}
        for country in countries_json:
            common_title = country.get("name").get("common")
            flag = country.get("flags").get("svg")
            common_lang = country.get('languages')
            if common_lang:
                common_language = list(country.get('languages').keys())[0]
            else:
                common_language = ""
            native_name = country.get("name").get("nativeName", None)
            if native_name:
                native_common_title = native_name.get(common_language, None)
                native_common = native_common_title.get("common") if native_common_title else ""
            else:
                native_common = ""
            if country.get("idd", None):
                phone_code = country.get("idd").get("root") + country["idd"]["suffixes"][0]
                country_phone_codes[common_title] = {"title": common_title,
                                                     "flag": flag,
                                                     "phone_code": phone_code,
                                                     "native_name": native_common}

    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return country_phone_codes


def write_codes_to_file():
    file_name = "countries_codes.json"
    country_codes = get_country_codes()
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(country_codes, f, ensure_ascii=False, indent=4)


write_codes_to_file()
