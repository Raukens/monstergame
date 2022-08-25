import random
import check
import pandas as pd
'''
name	level	energy	skills	points_to_next	monsters_list
'''
class Player:
    energy = 100
    points_to_next = 100
    level = 1
    skills = 0
    defeated_monsters = []

    def __init__(self, name):
        self.name = name

    def take_fight(self):

        win_prob = random.randrange(50, 90)
        damage = random.randrange(1, 40)
        if damage > (win_prob - 50):
            print("Вы низвергли монстра, он - мертв")
            self.energy = (self.energy - 10) * 1.2
            self.skills = self.skills + random.randrange(10, 50) * self.level * 1.5
            if self.points_to_next - self.skills > 0:
                self.points_to_next = self.points_to_next - self.skills
            else:
                self.level = self.level + 1
                self.points_to_next = abs(self.points_to_next - self.skills)
        else:
            print("Вы потерпели поражение")
            self.energy = self.energy - 10

    def refusal(self, name):
        self.energy -= 3

    def load(self):
        df = pd.read_csv('base.csv')
        if self.name in df['name']:
            index_sess = df.loc[df['name'].eq(self.name)].index
            self.name = df.iloc[index_sess, 0]
            self.level = df.iloc[index_sess, 1]
            self.energy = df.iloc[index_sess, 2]
            self.skills = df.iloc[index_sess, 3]
            self.points_to_next = df.iloc[index_sess, 4]



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
