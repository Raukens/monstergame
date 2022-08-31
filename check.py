import requests
import json
import random


def get_monsters():
    # source = 'https://ragnarokapi.bravan.cloudns.cl/monsters/?page=1&limit=100'
    # response = requests.get(source)
    #
    # if response.status_code == 200:
    #     print('Список монстров получен')
    #     return response
    # else:
    #     print("Не удается получить список монстров")

    with open("monsters.json") as json_file:
        data = json.load(json_file)

    return data


# list_mons = get_monsters()

# random_monster = random.choice(get_monsters())
# monster_name = random_monster['name']['en']
# print(monster_name)