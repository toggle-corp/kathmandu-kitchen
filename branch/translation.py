from modeltranslation.translator import translator, TranslationOptions
from branch.models import Branch, OpeningHour


class BranchTranslationOptions(TranslationOptions):
    fields = ('name', )


class OpeningHourTranslationOptions(TranslationOptions):
    fields = ('remarks', )


translator.register(Branch, BranchTranslationOptions)
translator.register(OpeningHour, OpeningHourTranslationOptions)
