from django.db import models
from django_markdown.models import MarkdownField


class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body_text = MarkdownField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return "{author}; {title}; {timestamp)".format(
            author=self.author,
            title=self.title,
            timestamp=self.timestamp,
        )
