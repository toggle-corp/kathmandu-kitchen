from modeltranslation.translator import translator, TranslationOptions
from branch.models import Branch


class BranchTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Branch, BranchTranslationOptions)
