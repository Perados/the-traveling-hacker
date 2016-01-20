from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse

from thetravelinghacker.blog.models import Post
from thetravelinghacker.blog.models import Reader

from thetravelinghacker.blog.forms import EmailForm

def home(request):
    return render_to_response('twitter.html')
