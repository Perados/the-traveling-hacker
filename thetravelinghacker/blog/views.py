from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse

from thetravelinghacker.blog.models import Post
from thetravelinghacker.blog.models import Reader

from thetravelinghacker.blog.forms import EmailForm


def home(request):
    posts = Post.objects.all().order_by('-timestamp')[:5]
    content = {'posts': posts}
    return render_to_response('index.html', content)


def about_me(request):
    return render_to_response('about-me.html')


def posts(request, post_id=None, post=None):
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return redirect('/')
        return redirect('/{}'.format(post.title.replace(' ', '-').lower()))

    try:
        previous_post = Post.objects.get(id=post.id-1)
    except Post.DoesNotExist:
        previous_post = None

    try:
        next_post = Post.objects.get(id=post.id+1)
    except Post.DoesNotExist:
        next_post = None

    form = EmailForm()

    return render_to_response('post.html', {'post': post, 'previous_post': previous_post, 'next_post': next_post, 'form': form})


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


@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        Reader.objects.create(email=email)

        subject = '[The Traveling Hacker] {} just subscribed'.format(email)

        send_mail(
            subject,
            subject,
            email,
            ['d.moracespedes@gmail.com'],
        )
        return HttpResponse()
