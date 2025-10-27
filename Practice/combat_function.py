#MW_CP1 combat function


import random

wizard = {
    "hp" : 45,
    "mana" : 100,
    "regen" : 50,
    "defence" : 0,
    "prowess" : 5,
    "fireball" : 20,
    "enscorche" : 5,
    "halo" : 20,
    "heal" : 5,
    "dazzle" : 5,
    "mimicing_scream" : random.randint(1,5),
    "crunch" : random.randint(1,10)
}

theif = {
    "hp" : 60,
    "defence" : 4,
    "prowess" : 10,
    "cloak" : 2,
    "cut" : random.randint(10,25),
    "heist" : random.randint(5, 20),
}

knight = {
    "hp" : 75,
    "defence" : 5,
    "prowess" : 5,
    "gaurd" : 2,
    "slash" : random.randint(10,12),
    "holy_light" : 8,
    "sheild_bash" : random.randint(5,10),
}

monster = {
    "hp" : 100,
    "defence" : 8,
    "prowess" : 0,
    "flail" : random.randint(10,20),
    "scream" : random.randint (1,3),
    "bite" : random.randint(15,25),
}

def attack(dmg, defence, prowess):
    if ((dmg + prowess) - defence) > (dmg/2):
        return dmg - defence
    elif ((dmg + prowess) - defence) < (dmg/2):
        return dmg / 2

def playerTurn(type):
    if type == wizard:
        pass
    elif type == theif:
        pass
    elif type == knight:
        pass

def monsterTurn(choice):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass



    