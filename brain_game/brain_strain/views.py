from django.template import RequestContext
from django.shortcuts import render, render_to_response
from brain_strain.models import Player
from json import dumps, loads
from django.http import HttpResponse
#from brain_strain.forms import CountryForm



# def add_country(request):
#     context = RequestContext(request)
#
#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#
#             return index(request)
#         else:
#             print form.errors
#     else:
#         form = CountryForm()
#
#     return render_to_response('brain_strain/add_country.html')


def index(request):
    context = RequestContext(request)

    context_dict = {'bold_message': " My brain does not hurt"}

    return render_to_response('brain_strain/index.html', context_dict, context)


#get help and ajax are the same, only ajax is an API


def get_help(request):
    context = RequestContext(request)

    player_list = Player.objects.all()

    context_dict = {'players_list': player_list}

    return render_to_response('brain_strain/get_help.html', context_dict, context)


def ajax(request):
    player_list = list(Player.objects.all())
    player_ajax_list = []
    for thePlayer in player_list:
        player_ajax_list.append({
            "fname": thePlayer.first_name,
            "lname": thePlayer.last_name,
            "uname": thePlayer.user_name,
        })

    return HttpResponse(dumps(player_ajax_list), content_type="application/json")


def players_list(request):
    context = RequestContext(request)

    player_list = Player.objects.all()

    context_dict = {'list_of_players': player_list}

    return render_to_response('brain_strain/players_list.html', context_dict, context)


def profile(request):
    context = RequestContext(request)

    profile_details = Player.objects.all()

    context_dict = {'profile_info': profile_details}

    return render_to_response('brain_strain/profile.html', context_dict, context)

#consuming ajax
def ajax_players(request):
    if request.method == "POST":
        aplayer = Player()
        aplayer.first_name = request.POST['first_name']
        aplayer.save()

    return render(request, 'brain_strain/ajax_players.html')
