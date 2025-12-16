#MW_CP1 final project


import random

#variables:

#Rin = {DICTIONARY of important things
rin = {
    #beastly lights collected : 1
    "lights" : 1,
    #hope : 30
    "hope" : 30,
    "max_hope" : 30,
    #lives
    "lives" : 3,
    #street lamps = []
    "street_lamps" : 0,
    #equip lantern : x
    "equipped_lantern" : "lantern",
    #equip light : y
    "equipped_light" : "flame",
    #rest point
    "rest point" : ["lumray_village", "1A"],
    #combo
    "combo" : 0,
    #agility
    "agility" : 3,
    #defense
    "defence" : 2,
    #turn
    "turns"  : 0,
    #effects
    "affects" : [],

    #lanterns : {DICTIONARY of lanterns
    "lanterns" : {
        #lantern : {DICTIONARY of the abilities of this lantern
        "lantern" : {
            "owned" : True,
            'abilities' : {
                "flail" : {
                    'description' : "1 hit for a good amount of dmg.",
                    'effect' : 'dmg',
                    'dmg' : random.randint(8,10)
                },

                "double flail" : {
                    'description' : "2 hits for a small amount of damage each",
                    'effect' : 'multidmg',
                    'dmg' : [random.randint(3,4), random.randint(3,4)]
                }
            }
        #}
        },

        #weighted_lantern : {DICTIONARY of the abilities of this lantern
        "weighted lantern" : {
            "owned" : False,
            'abilities' : {
                "slam" : {
                    'description' : "1 large slam",
                    'effect' : 'dmg',
                    'dmg' : random.randint(8,10)
                },

                "spinning strikes" : {
                    'description' : "3 hits for a lot of damage",
                    'effect' : 'multidmg',
                    'dmg' : [random.randint(5,8), random.randint(5,8), random.randint(5,8)]
                }
            }
        #}
        },
    },

    #}

    #lights = {DICTIONARY of all the lights and there effects
    "lights" : {
        #flame : {DICTIONARY of all the effects of this light
        "flame" :{
            "owned" : True,
            "abilities" : {
                'igniting burst' :{
                    'description' : "1 great strike that deals a huge chunk of damage!",
                    'effect' : "dmg",
                    'dmg' : random.randint(20,50)
                }
            }
        #}
        },
        #lightning : {DICTIONARY of all the effects of this light
        "lightning" : {
            "owned" : False,
            "abilities" : {
                'jolting strikes' :{
                    'description' : "6 large zaps of damage",
                    'effect' : "multidmg",
                    'dmg' : [random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15)]
                }
            }
        #}
        },
    #}
    },

    #MOVEMENT : {DICTIONARY of all different movement effects

    #}
}

#}



#Locations = {Dictionary of all locations on the map #how this works, the first key will be titled entrance and it will be attached to all the dialogues that might be described as well as all of the options of things to do, doing certain actions might eliminate the ability to do so and thus cause the player to need to see a different line og dialogue next time they enter. all of these rooms will have a dictionary within it, describing the locations that this room connects too, as well as all the requirments that the player might need to go to that specific room. they will then have key titled enemies which will either be False or have a specific enemy name attached to one of the enemies in the game this will allow for the room function to call a specific enemy as a function. then they will have a key titled Street lamp, the player will be able to ignite it allowing them to return to that location if they die (this value is either Ture or False) the next keys will all be optional to each room, and have specific things like whether or not this contains a light or ability pick up, and other similar things.
locations = {
    0 : {
        0 : 0
    },
    #Lumray Village : {DICTIONARY of rooms in town lands
    "lumray_village" :{
        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "1A" : {
            "enters" : 0,
            "street_lamp" : (True, False),
            "dialogue1" : "You wake up inside a cavern, a small lantern lays beside you, and in it there seems to be a small creature born in flame.",
            "dialogue2" : "You arrive at the same place you started The Street lamp still sits there, you still remember beeing here.",
            "events": False,
            "connections": (["lumray_village", "2A"],)
            #this room is a dark grotto with a small street lamp inside it, the player will get multiple lines of dialogue the player will be forced to ignite the lamp and then go left (This room attaches to "townlands"["2A"])
        #}
        },
        #2A {DICTIONARY of all important things in this room(including all rooms it connects too)
        "2A" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "As you continue forward you find small feirce frog, it is ready for battle!",
            "dialogue2" : "The green path beneath your feet is just as you remember, a new frog has taken its place! prepare for combat!",
            "events": {
                "enemy" : {
                    "oponent" : "small_frog",
                    "defeated" : False
                },

                "collectable" : False,
            },
            "connections": (["lumray_village", "1A"], ["lumray_village", "3A"],)
            #This room has a small enemy frog and will be used to have a mini tutorial about how to do basic combat same general style as room 1A (this room attaches to both "townlands"["1A"] and "townlands"["3A"])
        #}
        },
        #3A {DICTIONARY of all important things in this room(including all rooms it connects too)
        "3A" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "not much happens here, it's peicefull",
            "dialogue2" : False,
            "events": {
                "enemy" : False,

                "collectable" : False
            },
            "connections": (["lumray_village", "2A"], ["lumray_village", "1B"],["lumray_village", "2B"],)
            #this room contains a Large enemy Frog and will describe in mini tutorial format how complex combat works (connects to "townlands"["2A"] and "townlands"[2B])
        #}
        },
        #1B {Dictionary of all important things in this room (including all rooms it connects too)
        "1B" : {
            "enters" : 0,
            "street_lamp" : (True, False),
            "dialogue1" : "*kroooooooo* the flowing antlers of the beast are awe inspiring, but its beauty is not just gowing unanswered, its looking for a fight.",
            "dialogue2" : "You arrive at the foot of the town, the corpse of the glimmer beast still sitting there.",
            "events": {
                "enemy" : {
                    "oponent" : "glimmer_beast",
                    "defeated" : False,
                },

                "collectable" : False
            },
            "connections": (["roaring_peaks", "1A"], ["lumray_village", "2B"], ["lumray_village", "3B"])
            #this is the actual townlands, this room contains the glimmer beast(complex monster) after beating it the player will be able to teleport to all future ignited street lamps by going to a location with a street lamp, (this room connects to "Roaring peaks"["1A"] and "townlands"["2B"])
        #}
        },

        #2B {Dictionary of all important things in this room(including all rooms it connects too)
        "2B" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "You arrive at the small town. as you get there, lights crowd around you, you now have 2 extra agility in combat.",
            "dialogue2" : "you arrive at the small town.",
            "events": {
                "enemy": False,

                "collectable" : {
                    "stat": {
                        "collected" : False,
                        'stat_type' : 'agility',
                        'amount' : 2,
                    },

                    "lantern" : False,
                    "light" : False,
                }
            },
            "connections": (["lumray_village", "3A"], ["lumray_village", "1B"], ["lumray_village", "3B"])
            #, (connects to room "townlands"["1B"] and "townlands"["3B"])
        #}
        },
        #3B {Dictionary of all important things in this room(including all rooms it connects too)
        "3B" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "you arrive in a small alleyway with a hefty specimen lying down, you pick it up and now have the weighted lantern, you can select it at a street lamp.",
            "dialogue2" : "there used to be a lantern here",
            "events": {
                "enemy" : False,

                "collectable" : {
                    "stat" : False,
                    "lantern" : {
                        'collected' : False,
                        'lantern' : "weighted lantern"
                    },
                    "light" : False,
                }


            },
            "connections": (["lumray_village","2B"],['lumray_village',"1B"])
            #contains character Iyda an old ladie who wishes to see the town in its former state (connects to rooms "townlands"["2B"] and "townlands"["4B"])
        #}
        }
    #}
    },

    #Roaring peaks = {DICTIONARY of all rooms in this area
    "roaring_peaks" :{
        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "1A" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "you arrive at the beckoning high foothills of the mountains.",
            "dialogue2" : False,
            "events": False,
            "connections": (["lumray_village","1B"],['roaring_peaks',"2A"], ['roaring_peaks', '1B'])
            #this is the cross roads the player can take, they see a sign and the huge mountain above, they can either go up the roaring peaks, fo through the canyon to the beastly bellows or down to the fallen caverns (connects to rooms  townlands[1B] roaring peaks[2a] and beastly bellows[1A] - requires jolt jump| and fallen caverns[1A] - requires frost stride|)
        #}
        },
        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "2A" : {
            "enters" : 0,
            "street_lamp" : (True, False),
            "dialogue1" : "As you ascend the mountain you find a lantern, and light it! But electricity flows through you, bestowing a new resolve of hope.",
            "dialogue2" : "you find that place with the street lamp.",
            "events": {
                "enemy": False,

                "collectable" : {
                    "stat" : {
                        "collected" : False,
                        "stat_type" : "max_hope",
                        "amount" : 20
                    },
                    "lantern" : False,
                    "light" : False,
                }
            },
            "connections": (['roaring_peaks',"1A"], ['roaring_peaks', '3A'])
            #as you ascend you meet another friend Champ, he is determined to explore every avenue of the two mountain ranges, and you will meet him several times about your advntures (connects to rooms roaringpeaks[1A] and [3A])
        #}
        },
        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "3A" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "You find a small light laying on the ground, the light of lightning! if you would like to use it! go to a lantern and add it to your inventory!",
            "dialogue2" : "This is where you found the light of lightning",
            "events": {
                "enemy": False,

                "collectable" : {
                    "stat" : False,
                    "light" : {
                        "collected" : False,
                        "lighted" : "lightning"
                    },
                    "lantern" : False,
                }
            },
            "connections": (['roaring_peaks',"2A"],['roaring_peaks',"2B"])
            #This room contains a street lamp, but first you have to fight raging thunderbird(simple) (this room connects to roaring peaks[1b] and [2a] and [1c])
        #}
        },

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "1B" : {
            "enters" : 0,
            "street_lamp" : (True, False),
            "dialogue1" : "Glimmor surrounds you muscles, pain feals untouchable! your defence stat has been increased! There is also a lantern in here.",
            "dialogue2" : "A lantern is in here.",
            "events": {
                "enemy": False,

                "collectable" : {
                    "stat" : {
                        "collected" : False,
                        "stat_type" : "defence",
                        "amount" : 5
                    },
                    "lantern" : False,
                    "light" : False,
                }
            },
            "connections": (['roaring_peaks',"1A"],['roaring_peaks',"2B"])
            #this room has a battle with jolt flock(complex) (this room connects to raging peaks[3a] and [2B])
        #}
        },
        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)
        "2B" : {
            "enters" : 0,
            "street_lamp" : (False, False),
            "dialogue1" : "'Aha!' someone yells, 'I am going to destroy the world and send it too perpetual darkness!', they turn to you holding a large pair of scissors, you must kill them to save the kingdom!",
            "dialogue2" : False,
            "events": {
                "enemy": {
                    "defeated": False,
                    "oponent" : "scissor_dark"
                }
            },
            "connections": (['roaring_peaks',"1A"],['roaring_peaks',"2B"])
            #this room has a sign describing how most people who continue forwards often get struk by lightnign and get killed. (connects to rooms roaring peaks [1B] [3B] and [4B]- room requires thunder jump)
        #}
        }
    },

    1 : {
        1:1
    }
}

def restart():
    global rin
    global locations
    rin = {
        #beastly lights collected : 1
        "lights" : 1,
        #hope : 30
        "hope" : 30,
        "max_hope" : 30,
        #lives
        "lives" : 3,
        #street lamps = []
        "street_lamps" : 0,
        #equip lantern : x
        "equipped_lantern" : "lantern",
        #equip light : y
        "equipped_light" : "flame",
        #rest point
        "rest point" : ["lumray_village", "1A"],
        #combo
        "combo" : 0,
        #agility
        "agility" : 3,
        #defense
        "defence" : 2,
        #turn
        "turns"  : 0,
        #effects
        "affects" : [],

        #lanterns : {DICTIONARY of lanterns
        "lanterns" : {
            #lantern : {DICTIONARY of the abilities of this lantern
            "lantern" : {
                "owned" : True,
                'abilities' : {
                    "flail" : {
                        'description' : "1 hit for a good amount of dmg.",
                        'effect' : 'dmg',
                        'dmg' : random.randint(8,10)
                    },

                    "double flail" : {
                        'description' : "2 hits for a small amount of damage each",
                        'effect' : 'multidmg',
                        'dmg' : [random.randint(3,4), random.randint(3,4)]
                    }
                }
            #}
            },

            #weighted_lantern : {DICTIONARY of the abilities of this lantern
            "weighted lantern" : {
                "owned" : False,
                'abilities' : {
                    "slam" : {
                        'description' : "1 large slam",
                        'effect' : 'dmg',
                        'dmg' : random.randint(8,10)
                    },

                    "spinning strikes" : {
                        'description' : "3 hits for a lot of damage",
                        'effect' : 'multidmg',
                        'dmg' : [random.randint(5,8), random.randint(5,8), random.randint(5,8)]
                    }
                }
            #}
            },
        },

        #}

        #lights = {DICTIONARY of all the lights and there effects
        "lights" : {
            #flame : {DICTIONARY of all the effects of this light
            "flame" :{
                "owned" : True,
                "abilities" : {
                    'igniting burst' :{
                        'description' : "1 great strike that deals a huge chunk of damage!",
                        'effect' : "dmg",
                        'dmg' : random.randint(20,50)
                    }
                }
            #}
            },
            #lightning : {DICTIONARY of all the effects of this light
            "lightning" : {
                "owned" : False,
                "abilities" : {
                    'jolting strikes' :{
                        'description' : "6 large zaps of damage",
                        'effect' : "multidmg",
                        'dmg' : [random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15), random.randint(5,15)]
                    }
                }
            #}
            },
        #}
        },

        #MOVEMENT : {DICTIONARY of all different movement effects

        #}
    }

    #Locations = {Dictionary of all locations on the map #how this works, the first key will be titled entrance and it will be attached to all the dialogues that might be described as well as all of the options of things to do, doing certain actions might eliminate the ability to do so and thus cause the player to need to see a different line og dialogue next time they enter. all of these rooms will have a dictionary within it, describing the locations that this room connects too, as well as all the requirments that the player might need to go to that specific room. they will then have key titled enemies which will either be False or have a specific enemy name attached to one of the enemies in the game this will allow for the room function to call a specific enemy as a function. then they will have a key titled Street lamp, the player will be able to ignite it allowing them to return to that location if they die (this value is either Ture or False) the next keys will all be optional to each room, and have specific things like whether or not this contains a light or ability pick up, and other similar things.
    locations = {
        0 : {
            0 : 0
        },
        #Lumray Village : {DICTIONARY of rooms in town lands
        "lumray_village" :{
            #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "1A" : {
                "enters" : 0,
                "street_lamp" : (True, False),
                "dialogue1" : "You wake up inside a cavern, a small lantern lays beside you, and in it there seems to be a small creature born in flame.",
                "dialogue2" : "You arrive at the same place you started The Street lamp still sits there, you still remember beeing here.",
                "events": False,
                "connections": (["lumray_village", "2A"],)
                #this room is a dark grotto with a small street lamp inside it, the player will get multiple lines of dialogue the player will be forced to ignite the lamp and then go left (This room attaches to "townlands"["2A"])
            #}
            },
            #2A {DICTIONARY of all important things in this room(including all rooms it connects too)
            "2A" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "As you continue forward you find small feirce frog, it is ready for battle!",
                "dialogue2" : "The green path beneath your feet is just as you remember, a new frog has taken its place! prepare for combat!",
                "events": {
                    "enemy" : {
                        "oponent" : "small_frog",
                        "defeated" : False
                    },

                    "collectable" : False,
                },
                "connections": (["lumray_village", "1A"], ["lumray_village", "3A"],)
                #This room has a small enemy frog and will be used to have a mini tutorial about how to do basic combat same general style as room 1A (this room attaches to both "townlands"["1A"] and "townlands"["3A"])
            #}
            },
            #3A {DICTIONARY of all important things in this room(including all rooms it connects too)
            "3A" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "not much happens here, it's peicefull",
                "dialogue2" : False,
                "events": {
                    "enemy" : False,

                    "collectable" : False
                },
                "connections": (["lumray_village", "2A"], ["lumray_village", "1B"],["lumray_village", "2B"],)
                #this room contains a Large enemy Frog and will describe in mini tutorial format how complex combat works (connects to "townlands"["2A"] and "townlands"[2B])
            #}
            },
            #1B {Dictionary of all important things in this room (including all rooms it connects too)
            "1B" : {
                "enters" : 0,
                "street_lamp" : (True, False),
                "dialogue1" : "*kroooooooo* the flowing antlers of the beast are awe inspiring, but its beauty is not just gowing unanswered, its looking for a fight.",
                "dialogue2" : "You arrive at the foot of the town, the corpse of the glimmer beast still sitting there.",
                "events": {
                    "enemy" : {
                        "oponent" : "glimmer_beast",
                        "defeated" : False,
                    },

                    "collectable" : False
                },
                "connections": (["roaring_peaks", "1A"], ["lumray_village", "2B"], ["lumray_village", "3B"])
                #this is the actual townlands, this room contains the glimmer beast(complex monster) after beating it the player will be able to teleport to all future ignited street lamps by going to a location with a street lamp, (this room connects to "Roaring peaks"["1A"] and "townlands"["2B"])
            #}
            },

            #2B {Dictionary of all important things in this room(including all rooms it connects too)
            "2B" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "You arrive at the small town. as you get there, lights crowd around you, you now have 2 extra agility in combat.",
                "dialogue2" : "you arrive at the small town.",
                "events": {
                    "enemy": False,

                    "collectable" : {
                        "stat": {
                            "collected" : False,
                            'stat_type' : 'agility',
                            'amount' : 2,
                        },

                        "lantern" : False,
                        "light" : False,
                    }
                },
                "connections": (["lumray_village", "3A"], ["lumray_village", "1B"], ["lumray_village", "3B"])
                #, (connects to room "townlands"["1B"] and "townlands"["3B"])
            #}
            },
            #3B {Dictionary of all important things in this room(including all rooms it connects too)
            "3B" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "you arrive in a small alleyway with a hefty specimen lying down, you pick it up and now have the weighted lantern, you can select it at a street lamp.",
                "dialogue2" : "there used to be a lantern here",
                "events": {
                    "enemy" : False,

                    "collectable" : {
                        "stat" : False,
                        "lantern" : {
                            'collected' : False,
                            'lantern' : "weighted lantern"
                        },
                        "light" : False,
                    }


                },
                "connections": (["lumray_village","2B"],['lumray_village',"1B"])
                #contains character Iyda an old ladie who wishes to see the town in its former state (connects to rooms "townlands"["2B"] and "townlands"["4B"])
            #}
            }
        #}
        },

        #Roaring peaks = {DICTIONARY of all rooms in this area
        "roaring_peaks" :{
            #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "1A" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "you arrive at the beckoning high foothills of the mountains.",
                "dialogue2" : False,
                "events": False,
                "connections": (["lumray_village","1B"],['roaring_peaks',"2A"], ['roaring_peaks', '1B'])
                #this is the cross roads the player can take, they see a sign and the huge mountain above, they can either go up the roaring peaks, fo through the canyon to the beastly bellows or down to the fallen caverns (connects to rooms  townlands[1B] roaring peaks[2a] and beastly bellows[1A] - requires jolt jump| and fallen caverns[1A] - requires frost stride|)
            #}
            },
            #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "2A" : {
                "enters" : 0,
                "street_lamp" : (True, False),
                "dialogue1" : "As you ascend the mountain you find a lantern, and light it! But electricity flows through you, bestowing a new resolve of hope.",
                "dialogue2" : "you find that place with the street lamp.",
                "events": {
                    "enemy": False,

                    "collectable" : {
                        "stat" : {
                            "collected" : False,
                            "stat_type" : "hope",
                            "amount" : 20
                        },
                        "lantern" : False,
                        "light" : False,
                    }
                },
                "connections": (['roaring_peaks',"1A"], ['roaring_peaks', '3A'])
                #as you ascend you meet another friend Champ, he is determined to explore every avenue of the two mountain ranges, and you will meet him several times about your advntures (connects to rooms roaringpeaks[1A] and [3A])
            #}
            },
            #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "3A" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "You find a small light laying on the ground, the light of lightning! if you would like to use it! go to a lantern and add it to your inventory!",
                "dialogue2" : "This is where you found the light of lightning",
                "events": {
                    "enemy": False,

                    "collectable" : {
                        "stat" : False,
                        "light" : {
                            "collected" : False,
                            "lighted" : "lightning"
                        },
                        "lantern" : False,
                    }
                },
                "connections": (['roaring_peaks',"2A"],['roaring_peaks',"2B"])
                #This room contains a street lamp, but first you have to fight raging thunderbird(simple) (this room connects to roaring peaks[1b] and [2a] and [1c])
            #}
            },

            #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "1B" : {
                "enters" : 0,
                "street_lamp" : (True, False),
                "dialogue1" : "Glimmor surrounds you muscles, pain feals untouchable! your defence stat has been increased! There is also a lantern in here.",
                "dialogue2" : "A lantern is in here.",
                "events": {
                    "enemy": False,

                    "collectable" : {
                        "stat" : {
                            "collected" : False,
                            "stat_type" : "defence",
                            "amount" : 5
                        },
                        "lantern" : False,
                        "light" : False,
                    }
                },
                "connections": (['roaring_peaks',"1A"],['roaring_peaks',"2B"])
                #this room has a battle with jolt flock(complex) (this room connects to raging peaks[3a] and [2B])
            #}
            },
            #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)
            "2B" : {
                "enters" : 0,
                "street_lamp" : (False, False),
                "dialogue1" : "'Aha!' someone yells, 'I am going to destroy the world and send it too perpetual darkness!', they turn to you holding a large pair of scissors, you must kill them to save the kingdom!",
                "dialogue2" : False,
                "events": {
                    "enemy": {
                        "defeated": False,
                        "oponent" : "scissor_dark"
                    }
                },
                "connections": (['roaring_peaks',"1A"],['roaring_peaks',"2B"])
                #this room has a sign describing how most people who continue forwards often get struk by lightnign and get killed. (connects to rooms roaring peaks [1B] [3B] and [4B]- room requires thunder jump)
            #}
            }
        },

        1 : {
            1:1
        }
    }
    roomFunc('lumray_village','1A')
#}

def revive():
    rin["hope"] = rin["max_hope"]
    rin['lives'] = 3
    roomFunc(rin["rest point"][0], rin["rest point"][1])




#function for player turn combat: this first takes in what the player's current equipment is and thenuses that to set up the players actions, by 1 showing there current combo, 2 showing there current hope status and how many actions they have left, 3 looping over the dictionary of all there actions and checking what they would like to do.
def playerTurn(lantern, light, enemy):
    global rin
    options = {

    }
    actions = rin["agility"] - enemy["agility"] + rin["turns"]
    if actions <= 0:
        actions = 1
    rin["turns"] = 0
    actions
    while actions > 0:
        
        print(f"You currently have {rin['hope']} hope.\n You currently have {rin['lives']} crystaline recharges\n\n your current combo is {rin['combo']}           and you currently have {actions} moves left.")
        print(f"You currently have these actions available to you:")
        if rin["combo"] < 3:
            while True:
                chooses = 0
                for action in rin["lanterns"][lantern]["abilities"]:
                    chooses += 1
                    print(f"Press {chooses} if would like to use {action} it does {rin["lanterns"][lantern]['abilities'][action]['description']}")
                    options[chooses] = rin["lanterns"][lantern]['abilities'][action]
                choice = int(input("What you would you like to do? ").strip())
                if choice in range(1, chooses + 1):
                    if options[choice]['effect'] == 'dmg':
                        enemy['health'] -= (options[choice]['dmg'] - enemy['defence'])
                        rin["combo"] += 1
                        actions -= 1
                        break

                    if options[choice]['effect'] == 'multidmg':
                        for i in options[choice]['dmg']:
                            enemy['health'] -= i
                            rin["combo"] += 1
                        actions -= 1
                        break

        else:
            while True:
                chooses = 0
                for action in rin["lanterns"][lantern]["abilities"]:
                    chooses += 1
                    print(f"Press {chooses} if would like to use {action} it does {rin["lanterns"][lantern]['abilities'][action]['description']}")
                    options[chooses] = rin["lanterns"][lantern]['abilities'][action]
                
                for action in rin['lights'][light]["abilities"]:
                    chooses += 1
                    print(f"Press {chooses} if would like to use {action} it does {rin["lights"][light]['abilities'][action]['description']}")
                    options[chooses] = rin["lights"][light]['abilities'][action]

                choice = int(input("What you would you like to do? ").strip())
                if choice in range(1, chooses+1):
                    if options[choice]['effect'] == 'dmg':
                        enemy['health'] -= (options[choice]['dmg'] - enemy['defence'])
                        rin['combo'] += 1
                        actions -= 1
                        break

                    if options[choice]['effect'] == 'multidmg':
                        for i in options[choice]['dmg']:
                            enemy['health'] -= i
                            rin["combo"] += 1
                        actions -= 1
                        break

#function for monster turn combat (simple): this will take in the monsters action and do something with it, either dealing damage or applying a debuff or buff to themself.
def monsterTurn(monster):
    global rin
    options = {

    }
    chooses = 0

    actions = monster['agility'] - rin["agility"]
    if actions <= 0:
        actions = 1

    for action in monster['abilities']:
        chooses += 1
        options[chooses] = monster['abilities'][action]
    
    for i in range(actions):
        monster_choice = random.randint(1, chooses)

        if options[monster_choice]['effect'] == 'dmg':
            rin['hope'] -= (options[monster_choice]['dmg'] - rin['defence'])
            print(options[monster_choice]['description'])

        elif options[monster_choice]['effect'] == 'multidmg':
            for i in options[monster_choice]['dmg']:
                rin["hope"] -= i - rin["defence"]
            print(options[monster_choice]['description'])



        
    
#combat peice together: this will peice together all the combat functions for extremely simple use when attaching them to the many monster variables after this
def combat(monster):
    global rin
    while rin["lives"] > 0 and monster['health'] > 0:
        if rin['hope'] <= 0:
            rin['lives'] -= 1
            rin['hope'] = rin['max_hope']
            rin["combo"] = 0
            print("you have used a crystaline revive! and have lost your combo!")
        
        playerTurn(rin['equipped_lantern'], rin['equipped_light'], monster)

        print(monster["health"])

        monsterTurn(monster)
    else:
        if rin['lives'] == 0:
            while True:
                choice = input("You have died, would you like to resurect at your last lantern, if so press '1' (this keeps all your stuff just sets your location to the lantern)? Would you like to restart if so press '2'? Are you done?, if so press '3'.")
                if choice == '1':
                    roomFunc(rin["rest point"][0], rin["rest point"][1])
                    break
                elif choice == '2':
                    pass#call a restart function
                    break
                elif choice == '3':
                    roomFunc(0,0)
                    break
                else: 
                    print("make sure you use an number 1-3")
        elif monster['health'] <= 0:
            print("you have slain the monster!")

#function for each monster and there moves: each of these functions will set the monster variable (a dictionary) of all the things that are important for them, they will then call the combat peice together function and input there information into the function (there will be a lot of them)
def smallFrog():
    frog = {
        'health' : 200,
        'agility' : 1,
        'defence' : 1,
        'abilities' : {
            'slap' : {
                'description' : "\nThe Frog jumps up and slaps you!\n",
                'effect' : 'dmg',
                'dmg' : random.randint(5,8)
            },

            'hop_arouned' :{
                'description' : "\nThe frog jumps on you twice\n",
                'effect' : 'multidmg',
                'dmg' : [random.randint(2,6), random.randint(2,6)]
            }
        }
    }
    combat(frog)

def glimmerBeast():
    glimmer_beast = {
        'health' : 500,
        'agility' : 2,
        'defence' : 3,
        'abilities' : {
            'ram' : {
                'description' : "\nThe Beast rushes towards you, dealing a large amount of damage!\n",
                'effect' : 'dmg',
                'dmg' : random.randint(5,8)
            },

            'Kick' :{
                'description' : "\nThe Beast kicks you three times... ouch!\n",
                'effect' : 'multidmg',
                'dmg' : [random.randint(5,6), random.randint(10,12), random.randint(10,12)]
            },

            'glimmer_eplosion': {
                'description' : "\nThe Beast koos loudly before unleashing a large burst of damage\n",
                'effect' : 'dmg',
                'dmg' : random.randint(10,20)
            },
        }
    }
    combat(glimmer_beast)

def scissorDark():
    scissor_dark = {
        'health' : 500,
        'agility' : 2,
        'defence' : 2,
        'abilities' : {
            'snip' : {
                'description' : "\nshe cuts her foul scissors at you!\n",
                'effect' : 'dmg',
                'dmg' : random.randint(10,15)
            },

            'snip-snip' :{
                'description' : "\nshe cuts at you twice in quick succession YOUCH!!\n",
                'effect' : 'multidmg',
                'dmg' : [random.randint(2,10), random.randint(10,22)]
            },

            'darkness': {
                'description' : "\nShe leaves you feeling hopless!\n",
                'effect' : 'dmg',
                'dmg' : 29
            },
        }
    }
    combat(scissor_dark)


def equipment():
    print(f" your current lantern is the {rin['equipped_lantern']}\n\n your current light is {rin['equipped_light']}\n\n")
    while True:
        choice = int(input(f"Press '1' if you would like to change your lantern\n Press '2' if you would like to change your light\n Press '3' if you would like to leave this menu. "))
        if choice == 1:
            while True:
                choose = 0
                options = {

                }
                print("select a lantern:")
                for lantern in rin["lanterns"]:
                    if rin['lanterns'][lantern]["owned"] == True:
                        choose += 1
                        print(f"press {choose} to equip the: {lantern} as your weapon.")
                        options[choose] = lantern
                choice = int(input("Wich lantern would you like to equip? "))
                if choice in range(1,choose + 1):
                    rin["equipped_lantern"] = options[choice]
                    break
                else:
                    print(f"make sure you are pressing a number 1-{choose}, if it's not working, make sure you dont ahave anything else in the input, no letters or spaces.")
        elif choice == 2:
            while True:
                choose = 0
                options = {

                }
                print("select a light:")
                for light in rin["lights"]:
                    if rin['lights'][light]["owned"] == True:
                        choose += 1
                        print(f"press {choose} to equip the: {light} as your light.")
                        options[choose] = light
                choice = int(input("Wich light would you like to equip? "))
                if choice in range(1,choose + 1):
                    rin["equipped_light"] = options[choice]
                    break
                else:
                    print(f"make sure you are pressing a number 1-{choose}, if it's not working, make sure you dont ahave anything else in the input, no letters or spaces.")
        elif choice == 3:
            break
        else:
            print(f"Make sure you are pressing 1,2, or 3.")

        

#function for rooms: This will take in the dictionary of wich location you are in, how many times you have been in it, and what you can do in it (both what you have done and still can do), then it will take in the dictionary of all the places you can go too, and whether or not you have the movement to enter it.
def mover(biom, room):
    global locations
    global rin
    places = {

    }
    if rin["lives"] == 0:
        pass
    else:
        while True:
            options = 0
            if locations[biom][room]["street_lamp"] == (True, True):
                options += 1
                print(f"if you would like to access you inventory press {options}")
                options += 1
                print(f"if you would like to rest here press {options}")
            for i in locations[biom][room]["connections"]:
                options += 1
                print(f"press {options} to go to room {i[1]} inside biom {i[0]}.")
                places[options] = i

            choice = int(input("input where you would like to go: ").strip())
            if choice not in range(1, options+1):
                print(f"ensure you are pressing a number 1-{options}")
                pass
            if locations[biom][room]["street_lamp"] == (True, True):
                if choice == 1:
                    equipment()
                elif choice == 2:
                    rin["rest point"] = [biom, room]
                    rin["hope"] = rin['max_hope']
                    rin["lives"] = 3
                    print("you rest restoring your crystaline revitaslizers and hope.")
                elif choice in range(2, options+1):
                    roomFunc(places[choice][0], places[choice][1])
                    break
            else:
                if choice in range(1, options+1):
                    roomFunc(places[choice][0], places[choice][1])
                    break
                else:
                    print("make sure you are typing a correct input as listed above.")



def roomFunc(biom, room):
    global locations
    global rin
    if biom == 0:
        print("goodbye")
    elif biom == 1:
        print("you have won congrats!")
        while True:
            choice = input("press 1 to restart, press 2 to quite")
            if choice == "1":
                restart()
                break
            elif choice == 2:
                roomFunc(0,0)
                break


    else:
        if rin["lives"] == 0:
            pass
        else:
            if locations[biom][room]["enters"] == 0:
                print(locations[biom][room]["dialogue1"])
                locations[biom][room]["enters"] += 1
            elif locations[biom][room]["enters"] == 1 and locations[biom][room]["dialogue2"] != False:
                print(locations[biom][room]["dialogue2"])
            else:
                print(locations[biom][room]["dialogue1"])

            if locations[biom][room]["street_lamp"] == (True, False) and ((biom == "lumray_village" and room == "1A" ) is False):
                print("This room has Street lamp")
                locations[biom][room]["street_lamp"] = (True, True)
            elif locations[biom][room]["street_lamp"] == (True, False) and ((biom == "lumray_village" and room == "1A" ) is True):
                locations[biom][room]["street_lamp"] = (True, True)
            else:
                pass


            if locations[biom][room]["events"] == False:
                pass
            else:
                if bool(locations[biom][room]["events"]["enemy"]) == True:
                    if locations[biom][room]["events"]["enemy"]['oponent'] == "small_frog" and locations[biom][room]["events"]["enemy"]['defeated'] != True:
                        smallFrog()
                        locations[biom][room]["events"]["enemy"]['defeated'] = True
                    elif locations[biom][room]["events"]["enemy"]['oponent'] == "glimmer_beast" and locations[biom][room]["events"]["enemy"]['defeated'] != True:
                        glimmerBeast()
                        locations[biom][room]["events"]["enemy"]['defeated'] = True
                    elif locations[biom][room]["events"]["enemy"]['oponent'] == "scissor_dark" and locations[biom][room]["events"]["enemy"]['defeated'] != True:
                        scissorDark()
                        locations[biom][room]["events"]["enemy"]['defeated'] = True
                if rin["lives"] == 0:
                    pass
                else:
                    
                    if locations["roaring_peaks"]["2B"]["events"]["enemy"]['defeated'] == True:
                        roomFunc(1,1)
                        

                    if bool(locations[biom][room]["events"]["collectable"]) == True:
                        if bool(locations[biom][room]["events"]["collectable"]["stat"]) == True and locations[biom][room]["events"]["collectable"]["stat"]["collected"] == False:
                            rin[locations[biom][room]["events"]["collectable"]["stat"]["stat_type"]] += locations[biom][room]["events"]["collectable"]["stat"]["amount"]
                            locations[biom][room]["events"]["collectable"]["stat"]["collected"] = True
                        elif bool(locations[biom][room]["events"]["collectable"]["lantern"]) == True and locations[biom][room]["events"]["collectable"]["lantern"]["collected"] == False:
                            rin["lanterns"][locations[biom][room]["events"]["collectable"]["lantern"]['lantern']]["owned"] = True
                            locations[biom][room]["events"]["collectable"]["lantern"]['collected'] = True
                        elif bool(locations[biom][room]["events"]["collectable"]["light"]) == True and locations[biom][room]["events"]["collectable"]["light"]["collected"] == False:
                            rin["lights"][locations[biom][room]["events"]["collectable"]["light"]['lighted']]["owned"] = True
                            locations[biom][room]["events"]["collectable"]["light"]['collected'] = True
                    

            if rin["lives"] == 0:
                pass
            else:
                mover(biom, room)


roomFunc('lumray_village','1A')
    

    