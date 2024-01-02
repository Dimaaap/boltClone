from .filters import EqualFilter


def get_all_objects_from_db(db):
    return db.objects.all()


def filter_data_in_db(db, key: str, value: str):
    eq_filter = EqualFilter()
    return db.objects.filter(**eq_filter(key, value))


def is_field_exists(db, key: str, value: str):
    return filter_data_in_db(db, key, value).exists()