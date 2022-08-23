import random

import player
import check


def game():
    row = check.check_choices()
    gamer = player.Player(row)

    while gamer.energy < 0:

        random_monster = random.choice(check.get_monsters())
        monster_name = random_monster['name']['en']
        win_prob = random.randrange(50, 90)
        print(f"Вам попался {monster_name}. Вероятность победы - {win_prob}%")
        monster_choice = input("Если желаете с ним сразиться, то введите - 1, если выбрать другого, то - 2 ")
        if monster_choice == 1:
            print("Начинается игра")

            if damage() > (win_prob - 50):
                print("Вы низвергли монстра, он - мертв")
                self.energy = self.energy - 10
                self.skills = self.skills + random.randrange(10, 50) * self.level * 1, 5
                self.defeated_monsters.append(monster_name)
                if self.points_to_next - self.skills > 0:
                    self.points_to_next = self.points_to_next - self.skills
                else:
                    self.level = self.level + 1
                    self.points_to_next = abs(self.points_to_next - self.skills)
            else:
                print("Вы потерпели поражение")
                self.energy = self.energy - 10