from django.shortcuts import render_to_response

from thetravelinghacker.blog.models import Post


def home(request):
    posts = Post.objects.all().order_by('-timestamp')[:5]
    content = {'posts': posts}
    return render_to_response('index.html', content)


def about_me(request):
    return render_to_response('about-me.html')


def posts(request, post_id):
    post = Post.objects.get(id=post_id)
    return render_to_response('post.html', {'post': post})


def contact(request):
    return render_to_response('contact.html')