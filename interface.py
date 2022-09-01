import random
import keyboard

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

    while True:

        print("Начинается игра, для экстренного завершения нажмите -q")
        if gamer.energy < 0:
            break
        elif keyboard.is_pressed("q"):
            break

        monster = choose_monster()
        print(f"Вам попался {monster}")
        monster_choice = int(input(
            "Если желаете с ним сразиться, то введите - 1, "
            "если хотите выбрать другого, то - 2 "))
        monster_choice = services.is_number_proper(monster_choice, 1, 2)

        if monster_choice == 1:
            gamer.take_fight(monster)
        if monster_choice == 2:
            gamer.refusal()

    gamer.save_to_base()


if __name__ == '__main__':
    game()