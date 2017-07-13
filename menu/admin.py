from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline, \
    TranslationAdmin

from menu.models import MenuCategory, FoodTag, FoodItem


class FoodItemInline(TranslationStackedInline):
    model = FoodItem


class MenuCategoryAdmin(TranslationAdmin):
    inlines = [FoodItemInline]


admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(FoodTag)
