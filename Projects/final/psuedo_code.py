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

#Locations = {Dictionary of all locations on the map #how this works, the first key will be titled entrance and it will be attached to all the dialogues that might be described as well as all of the options of things to do, doing certain actions might eliminate the ability to do so and thus cause the player to need to see a different line og dialogue next time they enter. all of these rooms will have a dictionary within it, describing the locations that this room connects too, as well as all the requirments that the player might need to go to that specific room. they will then have key titled enemies which will either be False or have a specific enemy name attached to one of the enemies in the game this will allow for the room function to call a specific enemy as a function. then they will have a key titled Street lamp, the player will be able to ignite it allowing them to return to that location if they die (this value is either Ture or False) the next keys will all be optional to each room, and have specific things like whether or not this contains a light or ability pick up, and other similar things.

    #Lumray Village : {DICTIONARY of rooms in town lands

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room is a dark grotto with a small street lamp inside it, the player will get multiple lines of dialogue the player will be forced to ignite the lamp and then go left (This room attaches to "townlands"["2A"])
        #}

        #2A {DICTIONARY of all important things in this room(including all rooms it connects too)

            #This room has a small enemy frog and will be used to have a mini tutorial about how to do basic combat same general style as room 1A (this room attaches to both "townlands"["1A"] and "townlands"["3A"])
        #}

        #3A {DICTIONARY of all important things in this room(including all rooms it connects too)

            #this room contains a Large enemy Frog and will describe in mini tutorial format how complex combat works (connects to "townlands"["2A"] and "townlands"[2B])
        #}

        #1B {Dictionary of all important things in this room (including all rooms it connects too)

            #this is the actual townlands, this room contains the glimmer beast(complex monster) after beating it the player will be able to teleport to all future ignited street lamps by going to a location with a street lamp, (this room connects to "Roaring peaks"["1A"] and "townlands"["1B"])
        #}

        #2B {Dictionary of all important things in this room(including all rooms it connects too)

            #This room contains a street lamp, (connects to room "townlands"["1B"] and "townlands"["1C"])
        #}

        #3B {Dictionary of all important things in this room(including all rooms it connects too)

            #contains character Iyda an old ladie who wishes to see the town in its former state (connects to rooms "townlands"["2B"] and "townlands"["4B"])
        #}

        #4B {Dictionary of all important things in this room(including all rooms it connects too)

            #contains character Gette who really likes to fight, you can choose to fight him, or brush him off your choice, (connects to rooms "townlands"[3B] and "townlands"[5B])
        #}

        #5B {Dictionary of all important things in this room(including all rooms it connects too)
            
            #here you see the large feilds with the massive tower in the distance as well as the desolate peaks ahead (connects to rooms "townlands"[4B] and "soft meadows"[1A])
        #}
    #}

    #Roaring peaks = {DICTIONARY of all rooms in this area

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this is the cross roads the player can take, they see a sign and the huge mountain above, they can either go up the roaring peaks, fo through the canyon to the beastly bellows or down to the fallen caverns (connects to rooms  townlands[1B] roaring peaks[2a] and beastly bellows[1A] - requires jolt jump| and fallen caverns[1A] - requires frost stride|)
        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #as you ascend you meet another friend Champ, he is determined to explore every avenue of the two mountain ranges, and you will meet him several times about your advntures (connects to rooms roaringpeaks[1A] and [3A])
        #}

        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #This room contains a street lamp, but first you have to fight raging thunderbird(simple) (this room connects to roaring peaks[1b] and [2a] and [1c])
        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room has a battle with jolt flock(complex) (this room connects to raging peaks[3a] and [2B])
        #}

        #2B : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room has a sign describing how most people who continue forwards often get struk by lightnign and get killed. (connects to rooms roaring peaks [1B] [3B] and [4B]- room requires thunder jump)
        #}

        #3B : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room contains a street lamp (connects to rooms roaring peaks [2B] [5B] and [4C])
        #}

        #4B : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room contains a big fight with the last thunderKing, defeating this bird will allow you to collect the light of lightning (connects to room roaring peaks [2B])
        #}

        #5B : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #this room contains a fight with Zeri and Zips, a girl and her thunder bird(complex) defeating them will allow you to collect the ability Thunder jump (connects to room roaring peaks [3B])
        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #fight with a raging jolt bird (describes the desolation of the frigid peak ahead) (connects to rooms raging peaks [3a] and [2C])
        #}

        #2C : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #player a Frostling(simple) then they get to meet Champ again, (connects to rooms roaring peaks 1C and 4C and 3c)
        #}

        #3C : {DICTIONARY of all important things in room1(including all rooms it connects too)

            # contains a street lamp (connects to rooms 2c and 6c)
        #}

        #4C : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #simple fight with a frost strider (connects to rooms raging peaks 3b and 5C)
        #}

        #5C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #Here the player finds the tomb of beasts with five gems, depending on how many lights(beastly) the player has collected the tomb will show a different number of gems glowing, when all five are glowing, the player will be able to collect  the weighted lantern (connects to room 4c)
        #}

        #6C : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #The player finds a corps holding tightly onto a small egg, upon the player trying to grab it, combat will be initiated where the egg hatches and the player must tame the beast granting them the light of snow and frost stride (connects to roaring peaks 3c beasly bellows 10A)
        #}
    #}

    #beastly Bellows = {DICTIONARY of all rooms in Beasly bellows

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #player finds champ (he will be camping and either be ehausted or thrilled, deppending on when you run into him in the bellows) (connects to rooms roaring peaks 1A and beastly bellows 2a and 3a)
        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

            #connects to 
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

        #1A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #3A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #2C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

    #}

    #kings spire = {DICTIONARY of all rooms inside this area

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

        #1B : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #6A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1C : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1D : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1E : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #1F : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}

        #7A : {DICTIONARY of all important things in room1(including all rooms it connects too)

        #}
#}

#function for damage (dmg, receiver)
    
    #reveiver hp - dmg

#function for player turn combat: this first takes in what the player's current equipment is and thenuses that to set up the players actions, by 1 showing there current combo, 2 showing there current hope status and how many actions they have left, 3 looping over the dictionary of all there actions and checking what they would like to do.

#function for monster turn combat (simple): this will take in the monsters action and do something with it, either dealing damage or applying a debuff or buff to themself.

#function for monster turn combat (complex): this will have multiple attack types that will take in a players X and Y location to see if they aer going to get hit and print the feild in a way the player will understand how to dodge.

#combat peice together: this will peice together all the combat functions for extremely simple use when attaching them to the many monster variables after this

#function for each monster and there moves: each of these functions will set the monster variable (a dictionary) of all the things that are important for them, they will then call the combat peice together function and input there information into the function (there will be a lot of them)

#function for rooms: This will take in the dictionary of wich location you are in, how many times you have been in it, and what you can do in it (both what you have done and still can do), then it will take in the dictionary of all the places you can go too, and whether or not you have the movement to enter it.
