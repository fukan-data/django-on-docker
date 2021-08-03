from django import template

register = template.Library()

@register.simple_tag
def intcomma(num: int) -> str:
    if isinstance(num, int):
        return '{:,}'.format(num)
    else:
        return ''
