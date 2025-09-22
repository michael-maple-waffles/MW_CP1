#MW_CP1 User sighn in practice.



current_users = [("",""),]
current_usernames =["",]
username_identifier = ""
password_check = ""

class UserIdentity():
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def userRecal(self):
        print(f"\nWelcome {self.name}, have a good day!")

users = {
    
}

def userInterface():
    username_identifier = input("what is your username?\n")
    if username_identifier in current_usernames:
        password_check = input("What is your password?\n")
        full_user = (username_identifier,password_check)
        if full_user in current_users:
            users[username_identifier].userRecal()
        else:
            print("incorrect password.\n")
    else:
        yes_no = input("There is no account with this username. Would like to make an account? (input Y for yes and N for no)\n").capitalize().strip()
        if yes_no == "Y":
            username_identifier = input("what would you like your username to be?\n")
            password_check = input("What would you like your password to be?\n")
            current_users.append((username_identifier, password_check))
            current_usernames.append(username_identifier)
            users[username_identifier] = UserIdentity(username_identifier, password_check)
            users[username_identifier].userRecal()
        else:
            print("ok")

while True:
    userInterface()