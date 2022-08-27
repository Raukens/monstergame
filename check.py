import requests


def get_monsters():
    source = 'https://ragnarokapi.bravan.cloudns.cl/monsters/?page=1&limit=100'
    response = requests.get(source)

    if response.status_code == 200:
        print('Список монстров получен')
        return response
    else:
        print("Не удается получить список монстров")

