from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="contenturl")
@stringfilter
def contenturl(value):
    "Turns a full path into a content url"
    return value[21:]
