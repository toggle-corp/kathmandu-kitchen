from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline, \
    TranslationAdmin

from branch.models import Branch, OpeningHour


class OpeningHourInline(TranslationStackedInline):
    model = OpeningHour
    max_num = 7
    extra = 7


class BranchAdmin(TranslationAdmin):
    inlines = [OpeningHourInline]


admin.site.register(Branch, BranchAdmin)
