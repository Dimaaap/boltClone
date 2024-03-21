import base64

from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.exceptions import FieldDoesNotExist

from ..models import *
from ..data_storage import DataStorage
from ..db_services import get_data_from_model

data_storage = DataStorage()


def form_dropdown_cities_window():
    country_city_list = []
    for country in DriverCountries.objects.all():
        country_data = {
            "emoji": country.country_emoji_flag,
            "name": country.country_title,
            "cities": []
        }

        for city in DriverCities.objects.filter(country=country):
            country_data["cities"].append(city.city_title)
        country_city_list.append(country_data)
    sorted_country_list = sorted(country_city_list, key=lambda x: x["name"])
    sorted_country_list = sorted(sorted_country_list, key=lambda x: (x["name"] != "Україна", x["name"]))
    return sorted_country_list

class GetDriverInfoHelper:
    @staticmethod
    def get_driver_by_email_service(request):
        driver_email = request.session.get("email")
        driver = get_data_from_model(Driver, "driver_email", driver_email)
        return driver

    @staticmethod
    def get_driver_car_info_by_driver_service(driver):
        driver_car_info = get_data_from_model(DriverCarInfo, "driver_id", driver)
        return driver_car_info

    @staticmethod
    def get_driver_car_info_by_email_service(request):
        driver_email = request.session.get("email")
        driver = get_data_from_model(Driver, "driver_email", driver_email)
        driver_car_info = get_data_from_model(DriverCarInfo, "driver_id", driver)
        return driver_car_info


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def check_if_device_unique(request):
    print("Сheck if device in unique")
    driver_ip = get_client_ip(request)
    driver = get_data_from_model(Driver, "device_id", driver_ip)
    return driver and driver.is_verification


def is_user_in_db(email: str):
    return len(list(Driver.objects.filter(driver_email=email))) > 0



def get_user_last_registration_page(request):
    if request.session.get("on_second_page"):
        return "second"
    elif request.session.get("on_third_page"):
        return "third"
    return "first"


class FileUploadedHandler(GetDriverInfoHelper):

    @staticmethod
    def create_random_file_name_service() -> str:
        file_name = uuid4()
        return str(file_name)

    @staticmethod
    def decoded_request_body_service(file_url: str) -> ContentFile:
        image_format, image_str = file_url.split(";base64,")
        image_extension = image_format.split("/")[-1]
        data = base64.b64decode(image_str)
        file_name = FileUploadedHandler.create_random_file_name_service()
        image_file = ContentFile(data, name=f"{file_name}.{image_extension}")
        return image_file



    @staticmethod
    def save_file_in_model_service(request, field_name: str, exp_time: str, file_url: str) -> None:
        current_driver = GetDriverInfoHelper.get_driver_by_email_service(request)
        driver_car_info = GetDriverInfoHelper.get_driver_car_info_by_driver_service(current_driver)
        driver_docs = get_data_from_model(DriverCarDocuments, "driver_car_id", driver_car_info)
        file_data = FileUploadedHandler.decoded_request_body_service(file_url)
        try:
            image_model_field = DriverCarDocuments._meta.get_field(field_name)
        except FieldDoesNotExist:
            messages.error(request, "Сталась помилка")
        else:
            if field_name != "driver_photo":
                image_expiration_date = DriverCarDocuments._meta.get_field(f"{field_name}_expiration_time")
                if not driver_docs:
                    new_car_doc = DriverCarDocuments()
                    setattr(new_car_doc, image_model_field.name, file_data)
                    setattr(new_car_doc, image_expiration_date.name, exp_time)
                    new_car_doc.driver_car_id = driver_car_info
                    new_car_doc.save()
                else:
                    setattr(driver_docs, image_model_field.name, file_data)
                    setattr(driver_docs, image_expiration_date.name, exp_time)
                    driver_docs.save()
            else:
                if not driver_docs:
                    new_car = DriverCarDocuments.objects.create(driver_car_id=driver_car_info, driver_photo=file_data)
                    new_car.save()
                else:
                    setattr(driver_docs, "driver_photo", file_data)
                    driver_docs.save()
