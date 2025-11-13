#MW_CP1 order up!

#variables:

#checking = []
checking = []
#MENUE = Dictionary:
menu = {
    #MAINS: dictionary:
    "mains": {
        "Dirty Burger" :8.75,
        "Moo Moo Steak" :15.81,
        "Turkey Pot Pie" :10.56,
        "Skinny Girl Salad for one" :13.30,
        "Cluckers Famous CluckBurger" :12.21
    },
    
    #SIDES: dictionary:
    "sides" : {
        "Dirty Fries" :2.75,
        "Lettuce Salad" :5.22,
        "Turkey Toe Chips" :4.99,
        "Cluckers Famous Cluck Fries" :6.99,
        "Moo Moo chowder" :7.68,
        "Carols Tots" :3.00
    },

    #DRINKS: dictionary:
    "drinks": {
        "Dirty Coffee" :2.25,
        "Soft Drink" :1.25,
        "Cluckers Famous Cluck Coffee" :5.25,
        "Moo Moo Milk" :1.00,
        "Moo Moo Milk Strawberry" :1.50,
        "Moo Moo Milk Chocolate" :1.50,
        "Moo Moo Milk Cookie" :1.75,
        "Hand Pressed Orange Juice" :2.00
    },
    #Desserts : dictionary:
    "desserts" : {
        "Honey Punkin Pie" :4.50,
        "Bumble Bee Blue Berrie Pie" :4.50,
        "Golden Caramel Pecan Pie" :4.50,
        "Carol's Famous Cheescake" :4.50,
        "Garden Key Lime Pie" :4.50,
        "Garden Carrot Cake" :4.50,
    }
}
#ORDER = Dictionary:
order = {
    #MAINS: list:
    "mains" : [],

    #SIDES: list:
    "sides" :[],

    #DRINKS: list
    "drinks" :[],
    #DESSERTS : list:
    "desserts" :[],
    #PAYMENT : INT
    "payment" :0.00
}
#EMPLOYEES = Dictionary
employess = {
    #TIFFANY = Dictionary:
    "tiffany" : {
        #line1
        "welcome" : "So like Babe, welcome to carols diner, I am Tiffany! I hope you are having a good day, anyway I just wanted to say your vibe is like sOOooooOOOooo on point... but like guess I should like take your order.",
        #line2
        "mains" : "Ok babe, we have a lot of mains here so like choose wisely... I would reccomend you pick skinny girl salad for one, because like its SOOOooooOOOoo fetch. \n our totes delicous mains are:\n",
        #line3
        "sides" : "You Probably should like, pick a side, but I bet that you are like so cool you wont get any of that fatty high cholesteral stuff. \n We have:\n",
        #line4
        "drinks" : "Ok cutey, I know you prabably dont want this straight poison, but my mom makes me ask this,\n what drinks do you want?\n",
        #line5
        "desserts" : "I cant beleive this but, You should get dessert babe, I would reccomend you get famous cheesecake, my mom like works REALLY hard on it, but its like totes your choice.\n our desserts are:\n",
        #linewrong
        "linewrong" : "Babe Nuh UH, I dont understand whatever jibberish your speaking to me, make sure you say it exactly as I have listed:",
        #order done
        "orderdone" : "All right Babe! I will have that to you soon, just can I add you on insta? Sorry, my mom doesn't like when I do this, so I will just go get your food.",
        #ordercomplete
        "orderarrived" : "Here you go babe, have a day that is as feirce as you!"
    },
    #CAROL = Dictionary
    "carol" : {
        #line1
        "welcome" : "Welcome to my cafe Honey, I personally hope you're having a great day Honey.",
        #line2
        "mains" : "We have a lot of mains here at Carol's and so, Baby angel, take your time, \n we have:",
        #line3
        "sides" : "Alright Honey next up is your sides personally I like the tots, but its your choice honey,\n We have:\n",
        #line4
        "drinks" : "Honey baby angel we are sponsered by Moo Moo milk, so I would recomend them, but again not my choice,\n what drinks do you want?\n",
        #line5
        "desserts" : "Honey I dont care what you get for dessert, so long as you get some! All of the options are delicious, \n we have:\n",
        #linewrong
        "linewrong" : "Oh honey, we dont have that, make sure you type it exactly as I say.",
        #order done
        "orderdone" : "All right honey, that will be right with you.",
        #ordercomplete
        "orderarrived" : "Here you go honey, have a delicious day."
    },
    #DOUG = Dictionary
    "doug" : {
        #line1
        "welcome" : "Welcome to this gosh forsaken cafe.",
        #line2
        "mains" : "My ex thinks she is the star of the show just cause she made a successful diner and now I have to work my butt off here, because no where else is hiring.\n Anyway what would you like as your main?\n",
        #line3
        "sides" : "See the issue with this whole thing is that my daughter makes more money than I do here, that's my whole dog gone issue with this generation... oh you dont care? Sorry,\n for sides we have:\n",
        #line4
        "drinks" : "What do you want now? I wish I could have a beer gosh darn it, I wish I could curse but that witch is watching and she will cut my pay... you still dont care?\n Sorry, what drinks do you want?\n",
        #line5
        "desserts" : "The only thing good about this place is the dessert, but is a narcisistic kinda delicousness, it coresses your tongue just to take your whole gosh darn soul away... yeah I should see a therapist,\n For dessert we have:\n",
        #linewrong
        "linewrong" : "My ex wants you too say it exactly as I do, she won't take the order otherwise.",
        #order done
        "orderdone" : "That will be right with you.",
        #ordercomplete
        "orderarrived" : "I dont give a rats ash about your day or meal here, I already sent in my letter of resignation."
    }
}

#function that displays the menue DISPLAY(selection):

    #choices.append(selection)

    #for option in selection:

        #choices.append(option)

    #return choices


#function that shows the price of the selected dish PRICE(SELECTION)

    #for i in order[SELECTION]

        #order[PAYMENT] += Menue[Selection][i]

    #return order payment


#function that allows the user to select what they would like SELECT(SELECTION)

    #while True:

        #show emloyee's line for asking what dishes they would like

        #if item == "No":

            #break

        #elif item not in MENUE[SELECTION].keys():

            #employee reply item wrong

        #else: 

            #ORDER[SELECTION].append(item)
            #show current price is :PRICE(SELECTION)


#function that peices everything together PLAY(employee)

    #show: employees[employee]["line1"]

    #show DISPLAY("mains")

    #show employees[employee]["line2"]

    #show DISPLAY("sides")

    #show employees[employee]["line3"]

    #show DISPLAY("dinks")

    #show employees[employee]["line4"]

    #show DISPLAY("desserts")

    #show employees[employee]["order_complete"]

    #show employees[employee]["order_arrival"]



#SERVER = random.choice(employees.keys())

#PLAY(SERVER)