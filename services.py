import json

from player import Player


def is_number_proper(number, *args):
    while True:
        if number in args:
            break
        else:
            number = int(input("Введенное значение некорректно, повторите ввод: "))
    return number


def player_choice():
    x = int(input(
        "Для начала новой игры введите - 1, "
        "Для продолжения предыдущей сессии введите - 2, "
        "Для выхода введите - 3 "))
    return is_number_proper(x, 1, 2, 3)


def check_choices():
    nickname = input("Введите ник ")
    choice = player_choice()
    gamer = Player(nickname)
    try:
        with open(f"{nickname}.json") as json_file:
            data = json.load(json_file)
            existing_file = True
    except FileNotFoundError:
        existing_file = False

    if choice == 3:
        exit()
    if choice == 1:
        # df = df.append(add_new_player(name), ignore_index=True)
        print('Начинается новая игра')
    if choice == 2:
        if not existing_file:
            y = int(input(
                "У вас нет сохраненных сессий, для начала новой игры введите - 4 "
                "Для выхода введите - 3 "))
            inner_choise = is_number_proper(y, 3, 4)
            if inner_choise == 3:
                exit()
            if inner_choise == 4:
                print('Начинается новая игра')
        if existing_file:
            gamer = data
            # previous_session = df.loc[df['name'].str.contains(nickname)].copy
            # print(previous_session)
            # prev_sess_number = input("Введите номер сессии ")
            # '''копируем выбранную сессию в переменную'''
            # row = df.iloc[0].values.tolist()
    return gamer
