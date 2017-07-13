from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from branch.models import Branch


class BranchAdmin(TranslationAdmin):
    pass


admin.site.register(Branch, BranchAdmin)
