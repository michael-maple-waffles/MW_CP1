#MW_CP1 basic calculator


#Variables
number_1 = 0

number_2 = 0

yes_no = ""

option = ""

#functions
def calculator():
    global option
    global number_1
    global number_2
    yes_no = input(" Do you wish to use the calulator (input Y for Yes and N for No)").capitalize().strip()
    if yes_no == "Y":
        option = input("What form of math do you wish to use? Press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division, press 5 for integer division, press 6 for modulo division, press 7 for exponents.").capitalize().strip()
        if option == "1":
            number_1 = float(input("Input your first number"))
    elif yes_no == "N":
        breakpoint
    else:
        print("That was an invalid input")
        calculator()

while True:
    calculator()