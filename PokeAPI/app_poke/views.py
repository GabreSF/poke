import requests
from django.shortcuts import render

def pokemon_list(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    data = response.json()
    pokemons = data.get('results', [])

    pokemon_details = []

    for pokemon in pokemons:
        response = requests.get(pokemon['url'])
        if response.status_code == 200:
            pokemon_data = response.json()

            type_name = pokemon_data['types'][0]['type']['name']
            image_url = pokemon_data['sprites']['front_default']

            pokemon_details.append({
                'name': pokemon['name'],
                'type': type_name,
                'image_url': image_url,
            })

    selected_type = request.GET.get('type')  # Pega o tipo selecionado pelo usuário

    if selected_type and selected_type != 'all':
        filtered_pokemon_details = [pokemon for pokemon in pokemon_details if pokemon['type'] == selected_type]
    else:
        filtered_pokemon_details = pokemon_details

    context = {'pokemon_details': filtered_pokemon_details, 'selected_type': selected_type}
    return render(request, 'app_poke/index.html', context)
