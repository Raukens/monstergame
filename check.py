import pandas as pd
import requests

from player import Player


def get_monsters():
    source = 'https://ragnarokapi.bravan.cloudns.cl/monsters/?page=1&limit=100'
    response = requests.get(source)

    if response.status_code == 200:
        print('Список монстров получен')
        return response
    else:
        print("Не удается получить список монстров")


def is_number_proper(number, *args):
    while True:
        if number in args:
            break
        else:
            number = input("Введенное значение некорректно, повторите ввод: ")
    return number


def player_choice():
    x = input("Для начала новой игры введите - 1, Для продолжения предыдущей сессии введите - 2, \
                      Для выхода введите - 3")
    return is_number_proper(x, 1, 2, 3)


def check_choices():
    choice = player_choice()
    nickname = input("Введите ник ")
    df = pd.read_csv('base.csv')

    if choice == 3:
        exit()
    if choice == 1:
        # df = df.append(add_new_player(name), ignore_index=True)
        gamer = Player(nickname)
    if choice == 2:
        if df.empty or nickname not in df['name']:
            y = input("У вас нет сохраненных сессий, для начала новой игры введите - 4 \
                      Для выхода введите - 3 ")
            inner_choise = is_number_proper(y, 3, 4)
            if inner_choise == 3:
                exit()
            if inner_choise == 4:
                gamer = Player(nickname)
        if nickname in df['name']:
            gamer = Player.load(nickname)
            # previous_session = df.loc[df['name'].str.contains(nickname)].copy
            # print(previous_session)
            # prev_sess_number = input("Введите номер сессии ")
            # '''копируем выбранную сессию в переменную'''
            # row = df.iloc[0].values.tolist()
    return gamer

