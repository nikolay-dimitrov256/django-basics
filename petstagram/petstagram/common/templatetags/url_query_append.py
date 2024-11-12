from django import template

register = template.Library()


@register.simple_tag
def url_query_append(request, field, value):
    dictionary = request.GET.copy()
    dictionary[field] = value

    return dictionary.urlencode()
