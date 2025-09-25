#MW_CP1 classes in game



import random
from cave_adventure_libraries import stell

actions_left = 0

def stell_turn():
    if stell["boulderwing_vest"] == 1 and stell["starforce_dash"] == 1 and stell["hyper_jump"] == 1 and stell["star_power"] == 5 and stell["starshot_ready"] == True:
        stell_input = input(f"{stell["in_danger"]}.\n\n Child, you have {actions_left} actions left, your actions are:\n Press 1 for swipe (no movement, deals damage scaling with star power)\n Press 2 for dash (saves half of your actions rounded up for your next turn, ends all action)\n Press 3 for stellar strike (removes all actions, deals large damage based on steller power) \n Press 4 for Star Recersive (deals little dmg, and refunds current action)")


class AttackType:
    def __init__(self, row_display, row_dmg):
        self.row_display = row_display
        self.row_dmg = row_dmg
    
    def attack(self)
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
                print("-----|0\n-----|0\n-----|0\n!!!!!|2\nD::::|5")
                stell["in_danger"] = "You are currently under high danger"
            elif attack_type == 1 and stell["locate_y"] == 2:
                print("-----|0\n-----|0\n-----|0\nD!!!!|2\n:::::|5")
                stell["in_danger"] = "You are currently under minor danger"
            elif attack_type == 1 and stell["locate_y"] == 3:
                print("-----|0\n-----|0\nP----|0\n!!!!!|2\n:::::|5")
            elif attack_type == 1 and stell["locate_y"] == 4:
                print("-----|0\nP----|0\n-----|0\n!!!!!|2\n:::::|5")
            elif attack_type == 1 and stell["locate_y"] == 5:
                print("P----|0\n-----|0\n-----|0\n!!!!!|2\n:::::|5")
            elif attack_type == 2 and stell["locate_y"] == 1:
                print("-----|0\n!!!!!|2\n:::::|5\n!!!!!|2\nP----|0")
            elif attack_type == 2 and stell["locate_y"] == 2:
                stell["in_danger"] = "You are currently under minor danger"
                print("-----|0\n!!!!!|2\n:::::|5\nD!!!!|2\n-----|0")
        elif self.enemy_type == "wonderwing":
            pass
        elif self.enemy_type == "boulderwing":
            pass

rollytolli = Enemy("rollytolli", 5, False)

wonderwing = Enemy("wonderwing", 8, False)

boulderwing = Enemy("boulderwing", 35, False)