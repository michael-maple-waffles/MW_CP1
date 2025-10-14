#MW_CP1 password strength check.


#variables: 
    #password
password = ""
    #list of all special chars, titled CHAR
char = ["`", "~", "!", "@", "#", "$", "%","^","&","*","(", ")", "-","_", "=", "+","[","]","{","}","\\","|", "<",">",",",".",";",":","\"", "'"," ", "?","/"]
    #a dictionary that holds all past passwords PASSWORD_LIBRARY
password_library = {

}
    #a class variable with six values five being a boolean that is correlated to the five requirements, the sixth being its score. PASSWORD_QUALITIES 
class PasswordQualities:
    def __init__(self, length, uppercase, lowercase, number, special_char):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.number = number
        self.special_char = special_char
        self.points = length + uppercase + lowercase +number + special_char
    #a function will be in this to display the password and all of its qualities as well as how it can be inproved
    def pointProjection(self):
        self.points = self.length + self.uppercase + self.lowercase + self.number + self. special_char
    
        if self.length < 1:
            print("You need to have at least 8 characters.")
        if self.uppercase < 1:
            print("You need one uppercase letter.")
        if self.lowercase < 1:
            print("You need to have at least one lowercase letter,")
        if self.number < 1:
            print("You need at least one number.")
        if self.special_char < 1:
            print("You need at least one special character.")
        if self.points <= 1:
            print(f"Your password needs lots of work, it has {self.points} points.")
        elif self.points <= 3:
            print(f"Your password is ok, it has {self.points} points.")
        elif self.points <= 4:
            print(f"Your password is good, it has {self.points} points.")
        elif self.points == 5:
            print(f"Your password is perfect, it has {self.points} points")

        

#function to set up password to see if it meets requirments:
def requirementCheck():
    global password_library
    password = input("Input your password: ")
    #check len of password if its greater than or equal to 8, 
    #  than PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(LENGTH) = True PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(POINTS) += 1
    password_library[password] = PasswordQualities(0,0,0,0,0)
    if len(password) >=8:
        password_library[password].length = 1
    
    #for  LETTER in PASSWORD:
    for letter in password:
        #check if PASSWORD(letter) is upper
        if letter.isupper():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(UPPER) to true
            password_library[password].uppercase = 1
        #check if password(letter) is lower
        elif letter.islower():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(LOWER) to true
            password_library[password].lowercase = 1
        #check if PASSWORD(letter) is digit
        elif letter.isdigit():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(number) to true
            password_library[password].number = 1
        #check if PASSWORD(letter) is in CHAR
        elif letter in char:
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(special_char) to true
            password_library[password].special_char = 1
    
    password_library[password].pointProjection()

#a function to run the program
def run():
    global password_library
    print("This Program is going to test your password for how strong it is.\n\n")

    while True:
        yes_no = input("would you like to start testing your passwords?\n   (Y for yes, N for no): ").capitalize()

        if yes_no == "Y":
            
            while True:
                option = input(" Press 1 to input a password and have its strength checked\n Press 2 to veiw all current passwords, and the score they got\n Press 3 if you are finished testing your passwords\n (press 1, 2, or 3):").strip()
                if option == "1":
                    requirementCheck()
                elif option == "2" and bool(password_library) :
                    for keyword in password_library:
                        print(f"\nPassword: {keyword} Score: {password_library[keyword].points}")
                elif option == "2" and password_library == False:
                    print("You dont have any passwords yet.")
                elif option == "3":
                    break
                else:
                    print("Make sure you are inputting a number 1, 2, or 3.")

        elif yes_no == "N":
            print("goodbye!")
            break

        else:
            print("make sure you are using a Y or a N")

run()

