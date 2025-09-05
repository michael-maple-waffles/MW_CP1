#MW_CP1 Idiot proof project

#variables
first_name = ""
last_name = ""
phone_number = ""
gpa = 0.00

#functions
def numberValidation():
    phone_number = input("\n what is your phone number? \n").capitalize().strip()
    if " " not in phone_number and phone_number.isdigit() == True:
        if len(phone_number) == 10:
            print("valid phone number")
            phone_number.insert(3, " ")
            phone_number.insert(7, " ")
            print(phone_number)
        else:
            print("invalid phone number, make sure your phone number has 10 characters")
            numberValidation()
    else:
        print("invalid phone number, make sure you don't have any letters or spaces in your input.")
        numberValidation()




first_name = input("What is your name first name? \n").capitalize().strip()
last_name = input("\n What is your last name? \n").capitalize().strip()
numberValidation()

gpa = float(input("\n What is your gpa? \n").strip())

