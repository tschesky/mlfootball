from django import template
from django.template import Template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)