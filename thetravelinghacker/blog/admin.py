from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from thetravelinghacker.blog.models import Post


class PostAdmin(MarkdownModelAdmin):
    list_display = (
        'id',
    )

admin.site.register(Post, PostAdmin)
