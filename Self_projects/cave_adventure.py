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
    "locate_X" : 1,
    "locate_Y" : 1,
    #abilities
    "boulderwing_vest" : 0,
    "starforce_dash" : 0,
    "hyper_jump" : 0,
    "bubble_trouble" : 0,
    "starshot_power" : 0,
    
}

wonderwing = {
    "hp" : 10,
    "model" : "-/*\-",
    "location_x" : 0,
    "location_y" : 0,
    "dazzle" : random.randint(2,5),
}

boulderwing = {
    "hp" : 35,
    "model" : "/|\"
    "position" : "neither",
    "location_x" : 0,
    "location_y" : 0,
    "defeated" : False,
    "boulder_vest" : random.randint(1,3),
    "slam" : 8,
    "slam_miss" : 4,
    "falling_rubble" : 2,
    "swoop_claw" : 5,
    "swoop_miss" : random.randint(2,3),
}
