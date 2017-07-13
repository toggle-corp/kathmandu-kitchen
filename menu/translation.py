from modeltranslation.translator import translator, TranslationOptions
from menu.models import MenuCategory, FoodTag, FoodItem


class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class FoodTagTranslationOptions(TranslationOptions):
    fields = ('name', )


class FoodItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


translator.register(MenuCategory, MenuCategoryTranslationOptions)
translator.register(FoodTag, FoodTagTranslationOptions)
translator.register(FoodItem, FoodItemTranslationOptions)
