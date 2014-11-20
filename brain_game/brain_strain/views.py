from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)

    context_dict = {'bold_message': " My brain does not hurt"}

    return render_to_response('brain_strain/index.html', context_dict, context)
