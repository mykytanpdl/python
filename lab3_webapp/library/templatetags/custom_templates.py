from django import template

register = template.Library()

@register.filter
def getatt(obj, attr_name):
    """Returns the value of the object's attribute, or None if it doesn't exist."""
    return getattr(obj, attr_name, None)


@register.filter
def beautify(value):
    """Replaces underscores with spaces and capitalizes words"""
    return value.replace('_', ' ') if value.upper() == value \
        else value.replace('_', ' ').capitalize()