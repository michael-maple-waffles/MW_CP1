#MW_CP1 cave adventure


#import libraries
import random


#character variable
stell = {
    #basic things
    "hp" : 10,
    "swipe" : random.randint(3 ,5),

    #gameplay
    "location" : 0,
    "locate_Y" : 1,
    #abilities
    "boulderwing_vest" : 0,
    "starforce_dash" : 0,
    "hyper_jump" : 0,
    "bubble_trouble" : 0,
    "star_power" : 0,
    "starshot_ready" : False,
    
}

rollytolli = {
    "hp" : 5,
    "defeated" : False,
    "zoom" : 3,
    "zoom_bounce" : 5,
}

wonderwing = {
    "hp" : 8,
    "defeated" : False,
    "dazzle" : random.randint(2,5),
}

boulderwing = {
    "hp" : 35,
    "position" : "neither",
    "defeated" : False,
    "boulder_vest" : random.randint(1,3),
    "slam" : 8,
    "slam_miss" : 4,
    "falling_rubble" : 2,
    "swoop_claw" : 5,
    "swoop_miss" : random.randint(2,3),
}


