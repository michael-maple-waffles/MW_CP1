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
            print(f"Your password need lots of work, it has {self.points} points.")
        elif self.points <= 3:
            print(f"Your password is ok, it has {self.points} points.")
        elif self.points < 6:
            print(f"Your password is good, it has {self.points} points.")
        elif self.points == 6:
            print(f"Your password is perfect, it has {self.points} points")

        

#function to set up password to see if it meets requirments:
def requirementCheck():
    password = input("Input your password: ")
    #check len of password if its greater than or equal to 8, 
    #  than PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(LENGTH) = True PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(POINTS) += 1
    password_library[password] = PasswordQualities(0,0,0,0,0)
    if len(password) >=8:
        password_library[password].length = 1
    
    #for  LETTER in PASSWORD:
    for letter in password:
        #check if PASSWORD(letter) is upper
        if password(letter).isupper():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(UPPER) to true
            password_library[password].uppercase = 1
        #check if password(letter) is lower
        elif password(letter).islower():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(LOWER) to true
            password_library[password].lowercase = 1
        #check if PASSWORD(letter) is digit
        elif password(letter).isdigit():
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(number) to true
            password_library[password].number = 1
        #check if PASSWORD(letter) is in CHAR
            #if true add one point and set PASSWORD_LIBRARY[PASSWORD].PASSWORD_QUALITIES(special_char) to true

#a function to run the program
