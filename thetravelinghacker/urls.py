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
from django.conf.urls import include, url
from django.contrib import admin
from thetravelinghacker.blog.models import Post

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'thetravelinghacker.blog.views.home', name='home'),
    url(r'^about-me$', 'thetravelinghacker.blog.views.about_me', name='about_me'),
    url(r'^posts/(?P<post_id>[0-9]+)$', 'thetravelinghacker.blog.views.posts', name='posts'),
    url(r'^contact$', 'thetravelinghacker.blog.views.contact', name='contact'),
    url(r'^presentations/utbm$', 'thetravelinghacker.presentations.views.utbm', name='utbm'),
    url(r'^send-contact-mail', 'thetravelinghacker.blog.views.send_contact_mail', name='send_contact_mail'),
    url(r'^subscribe', 'thetravelinghacker.blog.views.subscribe', name='subscribe'),
    url(r'^twitter', 'thetravelinghacker.twitter.views.home', name='home'),
    url(r'^markdown/', include('django_markdown.urls')),
]

for post in Post.objects.all():
    urlpatterns.append(
        url(
            r'^{}'.format(post.title.replace(' ', '-').lower(), 'thetravelinghacker,blog.views.posts', name='posts'),
            'thetravelinghacker.blog.views.posts',
            {'post': post},
            name='posts',
        )
    )

