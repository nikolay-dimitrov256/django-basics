from django import template
from furryFunnies.common.helpers import get_profile

register = template.Library()


@register.simple_tag
def get_author():
    return get_profile()
