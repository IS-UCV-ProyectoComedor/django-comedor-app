from django.contrib import admin # type: ignore
from .models import Menu, MenuCategory, DailyMenu

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(DailyMenu)
