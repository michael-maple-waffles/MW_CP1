#ML 2nd Hello world project

#classify variables
name = [""]
name_input = ""
#inputs

while True:
    name_input = input("What is your name? ").capitalize().strip()

    if name_input in name:
        print("hello "+name_input+".")
    else:
        print("hello newbie.")
        name.append(name_input)