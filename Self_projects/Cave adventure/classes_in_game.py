#MW_CP1 classes in game

#enemy class
class Enemy:

    def __init__(self, enemy_type, hp, defeated,):
        self.enemy_type = enemy_type
        self.hp = hp
        self.defeated = defeated
    
    def battle(self):
        if self.enemy_type == "rollytolli":
            pass
        elif self.enemy_type == "wonderwing":
            pass
        elif self.enemy_type == "boulderwing":
            pass

rollytolli = Enemy("rollytolli", 5, False)

wonderwing = Enemy("wonderwing", 8, False)

boulderwing = Enemy("boulderwing", 35, False)