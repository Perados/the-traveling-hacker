from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify



class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body_text = MarkdownxField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return "{author}; {title}; {timestamp)".format(
            author=self.author,
            title=self.title,
            timestamp=self.timestamp,
        )

    @property
    def formatted_markdown(self):
        return markdownify(self.body_text)


class Reader(models.Model):
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return "{email)".format(
            timestamp=self.email,
        )
