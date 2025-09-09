#MW_CP1 basic calculator


#Variables
number_1 = 0.00

number_2 = 0.00

answer = 0.00

yes_no = ""

option = ""

off = 0

run = True

#functions
def calculator():
    global option
    global answer
    global number_1
    global number_2
    global off
    yes_no = input(" \n Do you wish to use the calulator (input Y for Yes and N for No)").capitalize().strip()
    if yes_no == "Y":
        option = input("\n What form of math do you wish to use? Press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division, press 5 for integer division, press 6 for modulo division, press 7 for exponents.\n").capitalize().strip()
        if option == "1":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 + number_2
            print(f"{number_1:.2f} + {number_2:.2f} = {answer:.2f}")
        elif option == "2":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 - number_2
            print(f"{number_1:.2f} - {number_2:.2f} = {answer:.2f}")
        elif option == "3":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 * number_2
            print(f"{number_1:.2f} x {number_2:.2f} = {answer:.2f}")
        elif option == "4":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 / number_2
            print(f"{number_1:.2f} / {number_2:.2f} = {answer:.2f}")
        elif option == "5":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 // number_2
            print(f"{number_1:.2f} // {number_2:.2f} = {answer:.2f}")
        elif option == "6":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 % number_2
            print(f"{number_1:.2f} % {number_2:.2f} = {answer:.2f}")
        elif option == "7":
            number_1 = float(input("Input your first number"))
            number_2 = float(input("Input your second number"))
            answer = number_1 ** number_2
            print(f"{number_1:.2f}^{number_2:.2f} = {answer:.2f}")
    elif yes_no == "N":
        return "end"
    else:
        print("That was an invalid input")
        calculator()


while True:
    run = calculator()
    print(run)
    if run == "end":
        break