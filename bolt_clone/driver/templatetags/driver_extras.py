from django import template

register = template.Library()


@register.filter(name="get_value")
def get_value(dictionary, key):
    field_value = dictionary.get(key, "")
    return shorten_file_name(field_value)


def shorten_file_name(file_name: str):
    file_name = str(file_name)
    split_file_name = file_name.split("/")
    return split_file_name[-1]


@register.filter(name="get_field_expiration_time")
def get_field_expiration_time(dictionary, key):
    return dictionary.get(key, "")


@register.filter(name="get_url_value")
def get_url_value(dictionary, key):
    file_loc = dictionary.get(key, "")
    if file_loc:
        return file_loc.url
    else:
        return ""