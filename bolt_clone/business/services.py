from django.core.exceptions import ObjectDoesNotExist

from .filters import EqualFilter


def get_data_from_model(model, field: str, value: str):
    eq_filter = EqualFilter()
    try:
        field = model.objects.get(**eq_filter(field, value))
    except ObjectDoesNotExist:
        return False
    return field