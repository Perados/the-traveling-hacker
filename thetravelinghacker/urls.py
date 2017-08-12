"""TheTravelingHacker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import logging

from django.conf.urls import include, url
from django.contrib import admin
from django.db.utils import ProgrammingError
from rest_framework import routers
from thetravelinghacker.blog.views import (
    home as blog_home,
    about_me,
    posts,
    contact,
    send_contact_mail,
    subscribe,
)
from thetravelinghacker.presentations.views import utbm
from thetravelinghacker.twitter.views import (
    TwitterUserViewSet,
    search_handle,
    home as twitter_home,
)
from thetravelinghacker.blog.models import Post

logger = logging.getLogger('django')

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'^twitter-users', TwitterUserViewSet, base_name='TwitterUsers')
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog_home, name='home'),
    url(r'^about-me$', about_me, name='about_me'),
    url(r'^posts/(?P<post_id>[0-9]+)$', posts, name='posts'),
    url(r'^contact$', contact, name='contact'),
    url(r'^presentations/utbm$', utbm, name='utbm'),
    url(r'^send-contact-mail', send_contact_mail, name='send_contact_mail'),
    url(r'^subscribe', subscribe, name='subscribe'),
    url(r'^search-handle', search_handle, name='search-handle'),
    url(r'^twitter/', twitter_home, name='twitter-home'),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^markdown/', include('django_markdown.urls')),
]

try:
    logger.info('There are "{}" posts in the database'.format(Post.objects.count()))
    for post in Post.objects.all():
        urlpatterns.append(
            url(
                r'^{}'.format(post.title.replace(' ', '-').lower(), posts, name='posts'),
                posts,
                {'post': post},
                name='posts',
            )
        )
except ProgrammingError:
    logger.info("The blog_post table is empty.")
