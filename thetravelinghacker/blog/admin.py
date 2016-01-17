from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from thetravelinghacker.blog.models import Post
from thetravelinghacker.blog.models import Reader


class PostAdmin(MarkdownModelAdmin):
    list_display = (
        'id',
    )

class ReaderAdmin(MarkdownModelAdmin):
    list_display = (
        'id',
        'email',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Reader,ReaderAdmin)
