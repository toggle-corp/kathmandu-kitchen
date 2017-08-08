from django.contrib import admin
from seo.models import MetaInformation, MetaKeyword


class MetaKeywordInline(admin.TabularInline):
    model = MetaKeyword
    extra = 2


class MetaInformationAdmin(admin.ModelAdmin):
    inlines = [MetaKeywordInline]


admin.site.register(MetaInformation, MetaInformationAdmin)
