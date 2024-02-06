from .models import ScooterReportModel, OtherReportModel


def save_report_to_model_service(form):
    (scooter_image, city, address,
     rent_company, other_rent_company, scooter_id, problem_desc) = (form.cleaned_data["scooter_image"],
                                                                    form.cleaned_data["city"],
                                                                    form.cleaned_data["address"],
                                                                    form.cleaned_data["rent_company"],
                                                                    form.cleaned_data["other_rent_company"],
                                                                    form.cleaned_data["scooter_id"],
                                                                    form.cleaned_data["problem_desc"])
    try:
        new_scooter_report = ScooterReportModel(scooter_img=scooter_image,
                                                city=city, address=address, rent_company=rent_company,
                                                other_rent_company=other_rent_company,
                                                scooter_id=scooter_id, problem_desc=problem_desc)
        new_scooter_report.save()
        print("Success")
    except Exception as e:
        print(e)
        form.add_error(problem_desc, "Помилка надсилання звіту")


def save_other_report_to_model(second_form):
    try:
        (rent_company, other_rent_company, problem_desc) = (
            second_form.cleaned_data["rent_company"], second_form.cleaned_data["other_rent_company"],
            second_form.cleaned_data["problem_desc"])
        new_report = OtherReportModel(rent_company=rent_company, other_rent_company=other_rent_company,
                                      problem_desc=problem_desc)
        new_report.save()
    except Exception as e:
        print(e)
        second_form.add_error("problem_desc", "Помилка зберігання форми")


def handle_first_form(form):
    if form.is_valid():
        save_report_to_model_service(form)
        success = True
    else:
        print("Form invalid")
        print(form.errors)
        success = False
    return success


def handle_second_form(second_form):
    if second_form.is_valid():
        save_other_report_to_model(second_form)
        success = True
    else:
        print(second_form.cleaned_data)
        success = False
    return success