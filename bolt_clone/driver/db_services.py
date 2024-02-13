from django.core.exceptions import ObjectDoesNotExist

from .filters import EqualFilter


def get_data_from_model(model, key, value):
    eq_filter = EqualFilter()
    try:
        data = model.objects.get(**eq_filter(key, value))
    except ObjectDoesNotExist:
        return None
    return data