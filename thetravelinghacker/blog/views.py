from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse
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

@csrf_exempt
def send_contact_mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = '[The Traveling Hacker] Message from ' + name + ': ' + email

        send_mail(
            subject,
            message,
            email,
            ['d.moracespedes@gmail.com'],
        )
        return HttpResponse()
