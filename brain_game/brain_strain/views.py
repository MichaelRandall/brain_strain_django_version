from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "My brain doesn\'t hurt"}

    return render_to_response('brain_strain/index.html', context_dict, context)
