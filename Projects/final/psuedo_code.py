#MW_CP1 Final Project Psuedo Code  ## hashs mean a maybe

#variables:

#Rin = {DICTIONARY of important things

    #witchly lights collected : 0

    #beastly lights collected : 1

    ##beasts tamed : 0

    #hope : 30

    ##hope collected : 30-60

    #lives : 1

    ###lives collected 1-3

    #city light : 0

    #city dim : 10

    #equip lantern : x

    #equip light : y

    #combo

    #lanterns : {DICTIONARY of lanterns

        #lantern : {DICTIONARY of the abilities of this lantern

        #}

        #weighted_lantern : {DICTIONARY of the abilities of this lantern

        #}

        #chainless lantern : {DICTIONARY of the abilities of this lantern

        #}

        #street lantern : {DICTIONARY of the abilities of this lantern

        #}
    #}

    #lights = {DICTIONARY of all the lights and there effects

        #flame : {DICTIONARY of all the effects of this light

        #}

        #lightning : {DICTIONARY of all the effects of this light

        #}

        #steam : {DICTIONARY of all the effects of this light

        #}

        #snow : {DICTIONARY of all the effects of this light

        #}

        #wind : {DICTIONARY of all the effects of this light

        #}

        #stars : {DICTIONARY of all the effects of this light

        #}

        #moon : {DICTIONARY of all the effects of this light

        #}

        #sun : {DICTIONARY of all the effects of this light

        #}
    #}

    #MOVEMENT : {DICTIONARY of all different movement effects

    #}
#}

#Locations = {Dictionary of all locations on the map

    #Lumray Village : {DICTIONARY of rooms in town lands

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A {DICTIONARY of all important things in this room(including all rooms it connects too)

        #}

        #3A {DICTIONARY of all important things in this room(including all rooms it connects too)

        #}

        #1B {Dictionary of all important things in this room (including all rooms it connects too)

        #}

        #2B {Dictionary of all important things in this room(including all rooms it connects too)

        #}

        #3B {Dictionary of all important things in this room(including all rooms it connects too)

        #}

        #4B {Dictionary of all important things in this room(including all rooms it connects too)

        #}

        #5B {Dictionary of all important things in this room(including all rooms it connects too)

        #}
    #}

    #Roaring peaks = {DICTIONARY of all rooms in this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #5B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #5C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #6C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
    #}

    #beastly Bellows = {DICTIONARY of all rooms in Beasly bellows

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #5A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #6A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #7A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #8A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #9A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #10A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
    #}

    #fallen caverns = {DICTIONARY of all rooms inside this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #5C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #6C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
    #}

    #soft meadows = {DICTIONARY of all rooms inside this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
    #}

    #Witches cauldren = {DICTIONARY of all rooms inside this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

    #}

    #Witches mansion = {DICTIONARY of all rooms inside this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #4B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #5B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
    #}

    #Witches Gathering = {DICTIONARY of all rooms inside this area
#}