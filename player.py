import random
import check


class Player:
    energy = 80
    points_to_next = 100
    level = 1
    skills = 0

    def __init__(self, name, *args):
        self.name = name
        self.defeated_monsters = list(args)

    def take_fight(self, name):
        player = Player(name)
        win_prob = random.randrange(50, 90)
        damage = random.randrange(1, 40)
        if damage > (win_prob - 50):
            print("Вы низвергли монстра, он - мертв")
            player.energy = player.energy - 10
            player.skills = player.skills + random.randrange(10, 50) * player.level * 1.5
            if player.points_to_next - player.skills > 0:
                player.points_to_next = player.points_to_next - player.skills
            else:
                player.level = player.level + 1
                player.points_to_next = abs(player.points_to_next - player.skills)
        else:
            print("Вы потерпели поражение")
            player.energy = player.energy - 10

        return [player.name, player.level, player.energy, player.skills, player.points_to_next]

    def refusal(self, name):

        player = Player(name)
        player.energy -= 3

        return [player.name, player.level, player.energy, player.skills, player.points_to_next]



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
