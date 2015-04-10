from django.contrib import admin
from cms.models import Blog_post

class Blog_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title',)}
    list_display = ('title',)

admin.site.register(Blog_post, Blog_postAdmin)