#MW_CP1 Who are you

#variables & Lists
user_dictionary = {

}


name_input = ""
name_container = [""]
color = ""
age = ""
#function to ask who they are
def whoAreYou():
    global name_container
    global name_input
    global user_dictionary
    global color
    global age
    name_input = input("What is your name? ").capitalize().strip()
    if name_input in name_container:
       print(user_dictionary[name_input])
    else:
        age = input("How old are you? ")
        color = input("What is your favorite Color? ")
        name_container.append(name_input)
        user_dictionary[name_input] = "Hello "+name_input+", you are "+age+" years old, and your favorite color is "+color+"."
        print(user_dictionary[name_input])
        name_container.append(name_input)
        

       

#while loop
while True:
    #series of if statements
    whoAreYou()
