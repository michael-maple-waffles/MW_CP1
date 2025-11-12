#MW_CP1 order up!

#variables:

#checking = []
checking = []
#MENUE = Dictionary:
menue = {
    #MAINS: dictionary:
    "mains": {
        "Dirty Burger" :8.75,
        "Moo Moo Steak" :15.81,
        "Turkey Pot Pie" :10.56,
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
oder = {
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

    #TIFFANY = Dictionary:

        #line1

        #line2

        #line3

        #line4

        #linewrong

        #order done

    #CAROL = Dictionary

        #line1

        #line2

        #line3

        #line4

        #linewrong

        #order done

    #DOUG = Dictionary

        #line1

        #line2

        #line3

        #line4

        #linewrong

        #order done

    #STONER JOE = dictoinary

        #line1

        #line2

        #line3

        #line4

        #linewrong

        #order done


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