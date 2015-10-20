from django.shortcuts import render_to_response

from thetravelinghacker.blog.models import Post


def home(request):
    blog_posts = Post.objects.all().order_by('-timestamp')[:5]
    content = {'blog_posts': blog_posts}
    return render_to_response('index.html', content)


def about_me(request):
    return render_to_response('about-me.html')


def posts(request):
    return render_to_response('posts.html')


def contact(request):
    return render_to_response('contact.html')