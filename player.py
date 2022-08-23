import pandas as pd
import requests
import random

import check





class Player:
    energy = 100

    def __init__(self, name, level, skills, points_to_next, *args):
        self.name = name
        self.level = level
        self.skills = skills
        self.points_to_next = points_to_next
        self.defeated_monsters = list(args)

    def damage():
        damage_player = random.randrange(1, 40)
        return damage_player
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





