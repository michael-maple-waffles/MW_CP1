#MW_CP1 shopping list


#Put your shopping list variable here

shopping_list = []

while True:
    action = input(f"If you would like to veiw your list if so press 1, \nIf you would like to add to your list press 2\nIf you would like to remove from your list press 3\nIf you would like to exit press 4: ").strip()
    #Write your code here
    if action == "1":
        print(f"\n\n Your shopping list contains:\n")
        for i in shopping_list:
            print(i)
        print(f"\n")

    elif action == "2":
        item = input(f"\nwhat would you like to add? ").strip().capitalize()
        if item not in shopping_list:
            shopping_list.append(item)
            print(f"\n\n Your shopping list contains:\n")
            for i in shopping_list:
                print(i)
            print(f"\n")
        else:
            print(f"\nThis item is already in the list\n")

    elif action == "3":
        item = input(f"\nwhat would you like to remove? ").strip().capitalize()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"\n\n Your shopping list contains:\n")
            for i in shopping_list:
                print(i)
            print(f"\n")
        else:
            print(f"\nThis item isn't in the list\n")

    elif action == "4":
        print("Powering Off")
        break

    else:
        print(f"\nmake sure your input is a 1, 2, 3, or 4.\n")