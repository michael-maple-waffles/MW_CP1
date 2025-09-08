#MW_CP1 basic calculator


#Variables
number_1 = 0

number_2 = 0

yes_no = ""

option = ""

#functions
def calculator():
    global option
    yes_no = input(" Do you wish to use the calulator (input Y for Yes and N for No)").capitalize().strip()
    if yes_no == "Y":
        option = input("What form of math do you wish to use? Press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division, press 5 for integer division, press 6 for modulo division, press 7 for exponents.").capitalize().strip()
    elif yes_no == "N":
        breakpoint
    else:
        print("That was an invalid input")
        calculator()

while True:
    