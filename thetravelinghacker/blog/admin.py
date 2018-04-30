from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from thetravelinghacker.blog.models import Post
from thetravelinghacker.blog.models import Reader

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Reader, MarkdownxModelAdmin)
