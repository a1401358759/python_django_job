from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
def game_list(request):
    dicts = {
        'game':Game.objects.order_by('date')[0:5]
    }
    return dicts
def player_list(request):
    players = {
        'player':Player.objects.order_by('id')[0:5]
    }
    return players
def index(request):
    message = 'I am index'
    return render_to_response(
        'game_index.html',
        locals(),
        context_instance = RequestContext(request,processors=[game_list,player_list])
        )

def types(request):
    message = 'I am types'
    return render_to_response(
        'types.html',
        locals(),
        context_instance = RequestContext(request,processors=[player_list])
        )

# Create your views here.
