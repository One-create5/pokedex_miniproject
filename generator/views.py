from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def pokedex(request):
    pokemon = request.GET.get('pokemon')
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(endpoint).json()
    
    game_name = res['name']
    game_index = res['game_indices'][3]['game_index']
    game_type = res['types'][0]['type']['name']
    game_weight = res['weight']
    game_height = res['height']
    game_sprit_front = res['sprites']['front_default']
    game_sprit_back = res['sprites']['back_default']

    return render(request, 'generator/pokedex.html', {'name': game_name, 'index':game_index,'type':game_type,'weight':game_weight,'height':game_height,'sprit_front_url':game_sprit_front,'sprit_back_url':game_sprit_back})
