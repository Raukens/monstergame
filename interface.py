import random

import check
import services
import player
from player import Player


def choose_monster():
    random_monster = random.choice(check.get_monsters())
    monster_name = random_monster['name']['en']
    return monster_name


def game():
    gamer = services.check_choices()

    while gamer.energy < 0:
        print("Начинается игра")
        monster = choose_monster()
        print(f"Вам попался {monster}")
        monster_choice = input("Если желаете с ним сразиться, то введите - 1, если хотите выбрать другого, то - 2 ")

        if monster_choice == 1:
            Player.take_fight(gamer.name)
        if monster_choice == 2:
            Player.refusal(gamer.name)
