from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
