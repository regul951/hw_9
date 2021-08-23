import requests
from pprint import pprint


api = '2619421814940190'
url = f'https://superheroapi.com/api/{api}/search/'


hero_dict = {}

for hero in ['Hulk', 'Captain America', 'Thanos']:
    id = requests.get(url+hero)
    hero_dict[hero] = id.json()['results'][0]['powerstats']['intelligence']

max_intl = max(hero_dict.items())


print(hero_dict, f'\nПобедил {max_intl[0]}, его интеллект равен {max_intl[1]}!')


