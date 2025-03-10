from django import template # type: ignore
from ..models import Menu 

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Get a Menu object by its ID, or return None if not found
    """
    try:
        return Menu.objects.get(menu_id=key)
    except Menu.DoesNotExist:
        return None 