from atexit import register
from django import template
from posts.models import card

register = template.Library()

@register.inclusion_tag('posts/Components/Header.html')

def get_last_post():
    first = card.objects.all().first
    return {'first': first}
