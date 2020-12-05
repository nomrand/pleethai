from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def get_settings(name):
    return getattr(settings, name, "")

@register.simple_tag
def get_map_settings(name, mapkey):
    map_var = getattr(settings, name, {})
    str_var = map_var.get(mapkey, '')
    return str_var
