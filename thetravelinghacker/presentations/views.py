from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse
from thetravelinghacker.blog.models import Post


def utbm(request):
    return render_to_response('utbm.html')