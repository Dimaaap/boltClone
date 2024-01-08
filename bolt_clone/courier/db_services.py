from .filters import EqualFilter


def get_all_fields_from_db(model):
    return model.objects.all()


def get_field_from_model(model, key, value):
    eq_filter = EqualFilter()
    return model.objects.get(**eq_filter(key, value))