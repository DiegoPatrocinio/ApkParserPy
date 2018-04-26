from django import template
from backoffice.models import *

register = template.Library()

@register.filter(name='counter_tags')
def counter_tags(values):
    qs = Article.objects.filter(hastag__name = values).count()
    return qs