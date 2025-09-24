#MW_CP1 classes in game



import random
from cave_adventure_libraries import stell

#enemy class
class Enemy:

    def __init__(self, enemy_type, hp, defeated,):
        self.enemy_type = enemy_type
        self.hp = hp
        self.defeated = defeated
    
    def battle(self):
        if self.enemy_type == "rollytolli":
            attack_type = random.randint (1,2)
            if attack_type == 1 and stell["locate_y"] == 1:
                print("-----0\n-----0\n-----0\n!!!!!2\nD::::5")
            elif attack_type == 1 and stell["locate_y"] == 2:
                print("-----0\n-----0\n-----0\nD!!!!2\n:::::5")
            elif attack_type == 1 and stell["locate_y"] == 3:
                print("-----0\n-----0\nP----0\n!!!!!2\n:::::5")
            elif attack_type == 1 and stell["locate_y"] == 4:
                print("-----0\nP----0\n-----0\n!!!!!2\n:::::5")
            elif attack_type == 1 and stell["locate_y"] == 5:
                print("P----0\n-----0\n-----0\n!!!!!2\n:::::5")
            elif attack_type == 2 and stell["locate_y"] == 1:
                print("-----0\n!!!!!2\n:::::5\n!!!!!2\nP----0")
        elif self.enemy_type == "wonderwing":
            pass
        elif self.enemy_type == "boulderwing":
            pass

rollytolli = Enemy("rollytolli", 5, False)

wonderwing = Enemy("wonderwing", 8, False)

boulderwing = Enemy("boulderwing", 35, False)