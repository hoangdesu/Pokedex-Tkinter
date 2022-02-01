import requests
import json

""" DATA NEEDED:
    - name
    - id
    - sprite: local (offline) link
    - height: in cm -> received data * 10
    - weight: in kg -> received data / 10
    - types: list of types
    - description: red version (https://pokeapi.co/api/v2/pokemon-species/{id})
    - evolution chain: [form1, form2, form3] (from https://pokeapi.co/api/v2/pokemon-species/id)
"""

POKEMON_BASE_URL = 'https://pokeapi.co/api/v2/pokemon'
EVOLUTION_CHAIN_URL = 'https://pokeapi.co/api/v2/evolution-chain'
POKEMON_SPECIES_URL = 'https://pokeapi.co/api/v2/pokemon-species'

total_pokemon = 151

def requestJSONdata() -> list:
    pokemon_list = []
    
    for i in range(total_pokemon):
        # getting basic info from base URL
        res = requests.get(f'{POKEMON_BASE_URL}/{i+1}')
        species_res = requests.get(f'{POKEMON_SPECIES_URL}/{i+1}')
        if res.status_code == 200 and species_res.status_code == 200: # status code 200 == success
            content = res.json()
            species_content = species_res.json()
            a_pokemon = {
                'name': content['species']['name'],
                'id': content['id'],
                'sprite': f'{i+1}.png',
                'height': content['height'] * 10,
                'weight': content['weight'] / 10,
                'types': [],
                'description': '',
                'evolution_chain': [],
            }
            
            for type in content['types']:
                a_pokemon['types'].append(type['type']['name'])
                
            
            # Extracting description such that lang name is 'en' and version is 'red'
            for entry in species_content['flavor_text_entries']:
                if entry['language']['name'] == 'en' and entry['version']['name'] == 'red':
                    # description = ''
                    # for char in entry['flavor_text']:
                    #     if char == '\n':
                    #         description += ' '
                    #     description += char
                    a_pokemon['description'] = entry['flavor_text'].replace('\n', ' ').replace('\x0c', ' ')
                    
                    
                    
                    
            # Sending request to Evolution chain
            evol_res = requests.get(species_content['evolution_chain']['url'])
            # print(evol_res.)
            if evol_res.status_code == 200:
                evol_content = evol_res.json()
                firstForm = evol_content['chain']['species']['name']
                a_pokemon['evolution_chain'].append(firstForm)
                if len(evol_content['chain']['evolves_to']) > 0:
                    secondForm = evol_content['chain']['evolves_to'][0]['species']['name']
                    a_pokemon['evolution_chain'].append(secondForm)
                    if len(evol_content['chain']['evolves_to'][0]['evolves_to']) > 0:
                        thirdForm = evol_content['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
                        a_pokemon['evolution_chain'].append(thirdForm)
                    
            pokemon_list.append(a_pokemon)
            # print(f'{a_pokemon["id"]}. {a_pokemon["name"]}', end=", ")
            
        else:
            print(f"Download error for pokemon {i+1}")

        print(a_pokemon['id'], a_pokemon['name'])

        
    return pokemon_list
        # pokemon_list.append(a_pokemon)
        # print(a_pokemon['name'], a_pokemon['id'])
        # print(a_pokemon['evolution_chain'])


    # // TODO: FIRST POKEMON WITH THE NEXT ID DON'T GET ADDED TO THE LIST OF EVOL CHAIN -> WHILE LOOP WOULD SOLVE
    # // TODO: CHECK IF THE FORM EXISTS FIRST BEFORE REQUESTING (SECOND AND THIRD FORMS)            
    # // TODO: CONVERT TRY-EXCEPT INTO CHECKING IF KEY EXISTS
    
    
def writeToJson(pokemon_list):
    with open('pokemon.json', 'w') as file:
        json.dump(pokemon_list, file, indent=4, ensure_ascii=False)
        file.close()
    
def downloadImages():
    for i in range(total_pokemon):
        url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i+1}.png'
        r = requests.get(url, allow_redirects=True)
        open(f'../sprites/{i+1}.png', 'wb').write(r.content)
        print(f'Downloaded sprite {i+1}')
    
def main():
    print('Start requesting JSON...')
    pokemon_list = requestJSONdata()
    print('Done requesting JSON. Start writing to json file...')
    writeToJson(pokemon_list)
    print('Successfully wrote to "pokemon.json". Start downloading sprites...')
    downloadImages()
    print('Download sprites done. Check the sprites folder')
    print('Download utility script completed! Your data is ready. Run the main program from "app.py"')
    
    

    
    # for poke in pokemon_list:
    #     print(f"{poke['id']}. {poke['name']} - Chain: {poke['evolution_chain']}")
    #     # print(poke)
    
    # with open('pokemon.json', 'w') as file:

    
if __name__ == '__main__':
    main()
    
    












""" Archived """

# def buildEvolutionChain(pokemon_list):
#     # build up evolution chain
#     evolution_chain_counter = 1
    
#     for i in range(len(pokemon_list)):
#         a_pokemon = pokemon_list[i]
#         pokeForms = []
#         evol_res = requests.get(f'{EVOLUTION_CHAIN_URL}/{evolution_chain_counter}')
#         evol_data = evol_res.json()


#         firstForm = evol_data['chain']['species']['name']
#         pokeForms.append(firstForm)
        
#         try:
#             secondForm = evol_data['chain']['evolves_to'][0]['species']['name']
#             pokeForms.append(secondForm)
#         except:
#             print(f"{pokemon_list[i]['name']} has no second form")
        
#         try:
#             thirdForm = evol_data['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
#             pokeForms.append(thirdForm)
#         except:
#             print(f"{pokemon_list[i]['name']} has no third form")
            
        
#         if a_pokemon['name'] in pokeForms:
#             # a_pokemon['evolution_chain'].append(firstForm)
#             # a_pokemon['evolution_chain'].append(secondForm)
#             # a_pokemon['evolution_chain'].append(thirdForm)
#             a_pokemon['evolution_chain'] = pokeForms
#         else:
#             evolution_chain_counter += 1
#             evol_res = requests.get(f'{EVOLUTION_CHAIN_URL}/{evolution_chain_counter}')
#             evol_data = evol_res.json()
            
#             # firstForm = evol_data['chain']['species']['name']
#             # secondForm = evol_data['chain']['evolves_to'][0]['species']['name']
#             # thirdForm = evol_data['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
            
        