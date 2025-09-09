#MW_CP1 Idiot proof project

#variables
first_name = ""
last_name = ""
phone_number = ""
gpa = 0.00
complete_phone_number = ""
cut_phone_number1 = ""
cut_phone_number2 = ""
cut_phone_number3 = ""
#functions
def numberValidation():
    global complete_phone_number
    phone_number = input("\n what is your phone number? (do not include spaces or dashes) \n").capitalize().strip()
    if " " not in phone_number and phone_number.isdigit() == True:
        if len(phone_number) == 10:
            print("valid phone number")
            cut_phone_number1 = phone_number[:3]
            cut_phone_number2 = phone_number[3:6]
            cut_phone_number3 = phone_number[6:10]
            complete_phone_number = cut_phone_number1 + " " + cut_phone_number2 + " " + cut_phone_number3
            print(complete_phone_number)
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

print("Hello, " +first_name+ " "+last_name+". your phone number is " +complete_phone_number+ ", and your gpa is a " +str(gpa)".")

