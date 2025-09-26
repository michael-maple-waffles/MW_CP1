#MW_CP1 classes in game



import random
from cave_adventure_libraries import stell

actions_left = 0

actions_saved = 0






class AttackType:
    def __init__(self, row_display, row_dmg):
        self.row_display = row_display
        self.row_dmg = row_dmg
    
    def attack(self, dmg_zone_high, dmg_zone_low):
        if stell["locate_Y"] == 1 and stell["locate_Y"] not in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\nP{self.row_display[5]}")
            stell["in_danger"] = "You are not currently in danger"

        elif stell["locate_Y"] == 1 and stell["locate_Y"] in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\nD{self.row_display[5]}")
            stell["in_danger"] = "You are currently in danger"

        elif stell["locate_Y"] == 2 and stell["locate_Y"] not in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\nP{self.row_display[4]}\n-{self.row_display[5]}\n\n")
            stell["in_danger"] = "You are not currently in danger"

        elif stell["locate_Y"] == 2 and stell["locate_Y"] in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\nD{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are currently in danger"

        elif stell["locate_Y"] == 3 and stell["locate_Y"] not in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\nP{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are not currently in danger"

        elif stell["locate_Y"] == 3 and stell["locate_Y"] in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\n-{self.row_display[2]}\nD{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are currently in danger"
        
        elif stell["locate_Y"] == 4 and stell["locate_Y"] not in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\nP{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are not currently in danger"

        elif stell["locate_Y"] == 4 and stell["locate_Y"] in (dmg_zone_high or dmg_zone_low):
            print(f"-{self.row_display[1]}\nD{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are currently in danger"

        elif stell["locate_Y"] == 5 and stell["locate_Y"] not in (dmg_zone_high or dmg_zone_low):
            print(f"P{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are not currently in danger"
        
        elif stell["locate_Y"] == 5 and stell["locate_Y"] in (dmg_zone_high or dmg_zone_low):
            print(f"D{self.row_display[1]}\n-{self.row_display[2]}\n-{self.row_display[3]}\n-{self.row_display[4]}\n-{self.row_display[5]}")
            stell["in_danger"] = "You are currently in danger"

        
        
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

rollytolli = Enemy("rollytolli", 6, False)

def stell_turn (monster):
    global actions_left
    global actions_saved

    while actions_left > 0:
        if stell["boulderwing_vest"] == 1 and stell["starforce_dash"] == 1 and (stell["hyper_jump"] == 1 and stell["locate_Y"] ==1) and stell["bubble_trouble"] == 1 and stell["star_power"] == 5 and stell["starshot_ready"] == 3:
            stell_input = input(f"{stell["in_danger"]}.\n\n Starshot: ready \n\n Child, you have {actions_left} actions left, your actions are:\n\n Press 1 for swipe (you will fall one, deals damage scaling with star power)\n Press 2 for jump (sends you up two)\n Press 3 for dash (saves half of your actions rounded up for your next turn, ends all action)\n Press 4 for stellar strike (causes you to fall one, removes all actions, deals large damage based on steller power) \n Press 5 for Star Recersive (deals little dmg, and refunds current action, beware using this will hurt you will also fall one)\n Press 6 for great slam (slams you to the ground, dealing damage based on how far you fell)\n Press 7 for upward starforce dash (A regular dash, but you move up once)\n Press 8 for downward starforce dash (A regular dash, but you move down once)\n Press 9 for hyper jump (a jump that puts you in the ceiling, can only be used on the ground)\n Press 10 for bubble trouble (holds you where you are)\n Press 11 for Starshot (Deals extremely high amounts of damage takes time to recharge)")
            if stell_input == "1":
                monster.hp -= stell["swipe"] + stell["star_power"]
                stell["locate_Y"] -= 1
                actions_left -= 1
            elif stell_input == "2":
                stell["locate_Y"] += 2
                actions_left -= 1
            elif stell_input == "3":
                actions_saved = round(actions_left / 2)
                actions_left = 0
            elif stell_input == "4":
                monster.hp -= (2 * actions_left)+stell["stellar_strike"] 