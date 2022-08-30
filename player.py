import random
import json

'''
name	level	energy	skills	points_to_next	monsters_list
'''


class Player:
    energy = 100
    points_to_next_lvl = 100
    level = 1
    points = 0
    points_of_level = 100
    defeated_monsters = []

    def __init__(self, name):
        self.name = name

    def take_fight(self, monster_name):

        win_prob = random.randrange(49, 90)
        damage = random.randrange(0, 100)

        if damage > 100 - win_prob:
            self.energy = (self.energy - 10) * 1.2
            self.points += random.randrange(10, 50)
            if self.points_to_next_lvl - self.points > 0:
                self.points_to_next_lvl -= self.points
            else:
                self.level += 1
                self.points_of_level *= 1.5
                self.points_to_next_lvl = self.points_of_level - abs(self.points_to_next_lvl - self.points)
                self.defeated_monsters.append(monster_name)
            print(
                f"Вы низвергли монстра, уровень вашей энергии - {self.energy}, "
                f"опыта - {self.points}, очков до следующего уровня{self.points_to_next_lvl}")
        else:
            self.energy -= 10
            print(f"Вы потерпели поражение, ваша энергия снизилась до {self.energy}")

    def refusal(self):
        self.energy -= 3
        print(f"Ваш уровень энергии снизился до {self.energy}")

    def save_to_base(self):
        with open(f"'{self.name}.json', 'w'") as base:
            json.dump({
                "name": self.name,
                "level": self.level,
                "skills": self.points,
                "points_to_next": self.points_to_next_lvl,
                "energy": self.energy,
                "points_of_level": self.points_of_level,
                "monsters_list": self.defeated_monsters
            }, base)



'''

[{"name":{"ptBr":"Escorpião","en":"Scorpion"},"id":1001},
 {"name":{"ptBr":"Poring","en":"Poring"},"id":1002},
 {"name":{"ptBr":"Zangão","en":"Hornet"},"id":1004},
 {"name":{"ptBr":"Familiar","en":"Familiar"},"id":1005},
 {"name":{"ptBr":"Fabre","en":"Fabre"},"id":1007},
 {"name":{"ptBr":"Pupa","en":"Pupa"},"id":1008},
 {"name":{"ptBr":"Condor","en":"Condor"},"id":1009},
 {"name":{"ptBr":"Salgueiro","en":"Willow"},"id":1010},
 {"name":{"ptBr":"ChonChon","en":"Chonchon"},"id":1011},
 {"name":{"ptBr":"Sapo de Rodda","en":"Roda Frog"},"id":1012}]

'''
