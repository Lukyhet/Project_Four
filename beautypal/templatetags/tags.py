from django import template

register = template.Library()

@register.filter
def url_safe(value):
    return value.replace(" ","%20")