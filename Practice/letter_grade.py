#MW_CP1 letter garde assighnment.


grade = 0.00

yn = ""

grade_class = ""

grades_input = {

}

def grade_check():
    grade_class = input("what class is this in?").strip()
    grade = float(input("what if your grade as a number (input your grade as a number)\n").strip())
    if grade >= 94.00:
        grades_input[grade_class] = "A"
        print("congrats you have an A!")
    elif grade >= 90:
        grades_input[grade_class] = "A-"
        print("congrats you have an A-!")
    elif grade >= 84:
        grades_input[grade_class] = "B"
        print("you have a B")
    elif grade >= 80:
        grades_input[grade_class] = "B-"
        print("You Have a B-.")
    elif grade >= 74:
        grades_input[grade_class] = "c"
        print("You Have a c.")
    elif grade >= 70:
        grades_input[grade_class] = "c-"
        print("You Have a c-")
    else:
        grades_input[grade_class] = "F"
        print("You Have an F.")

while True:
    yn = input("would you like to use this program? (Y/N)\n").strip().capitalize()
    if yn == "Y":
        grade_check()
    elif yn == "N":
        print("Have a good day.")
        break
    else:
        print("you made a wrong input, make sure you input a capital Y or N.")