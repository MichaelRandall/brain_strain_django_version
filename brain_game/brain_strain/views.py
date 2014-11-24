from django.template import RequestContext
from django.shortcuts import render_to_response
from brain_strain.models import Player


def index(request):
    context = RequestContext(request)

    context_dict = {'bold_message': " My brain does not hurt"}

    return render_to_response('brain_strain/index.html', context_dict, context)


def help(request):
    return HttpResponse("Rango says, here is about page <a href = 'http://localhost:8000/rango/'>stuff</a>")


def profile(request):
    return HttpResponse("Rango says, here is about page <a href = 'http://localhost:8000/rango/'>stuff</a>")


def settings(request):
    return HttpResponse("Rango says, here is about page <a href = 'http://localhost:8000/rango/'>stuff</a>")


def start(request):
    return HttpResponse("Rango says, here is about page <a href = 'http://localhost:8000/rango/'>stuff</a>")