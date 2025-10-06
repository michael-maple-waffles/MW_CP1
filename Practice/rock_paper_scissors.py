#MW_CP1 rock paper scissors


import random 
wins = 0
losses = 0
plr_wins = 0
bot_wins = 0
ties = 0
plays = 0

def turn():
    plr_wins = 0
    bot_wins = 0
    ties = 0

    global losses
    global wins
    global plays

    while plr_wins < 2 and bot_wins < 2:

        bot_choice = random.randint(1,3)

        print(f"You have currently won {plr_wins} times, I have won {bot_wins} times, we have tied {ties} times.\n")

        choice = input("press 1 for rock, press 2 for paper, and press 3 for scissors\n").strip()

        if choice == "1" and bot_choice == 3:
            print("\nyou put rock, and I put scissors, you win!\n")
            plr_wins += 1

        elif choice == "1" and bot_choice == 2:
            print("\nYou put rock, I put paper, I win!\n")
            bot_wins += 1

        elif choice == "1" and bot_choice == 1:
            print("\nYou put rock, I put rock, we tied.\n")
            ties += 1

        elif choice == "2" and bot_choice == 3:
            print("\nYou put paper, I put scissors, I win!\n")
            bot_wins += 1
        
        elif choice == "2" and bot_choice == 2:
            print("\nYou put paper, I put paper, we tied.\n")
            ties += 1

        elif choice == "2" and bot_choice == 1:
            print("\nYou put paper, I put rock, You win!\n")
            plr_wins += 1

        elif choice == "3" and bot_choice == 3:
            print("\nYou put scissors, I put scissors, we tied.\n")
            ties += 1

        elif choice == "3" and bot_choice == 2:
            print("\nYou put scissors, I put paper, You win!\n")
            plr_wins += 1

        elif choice == "3" and bot_choice == 1:
            print("\nYou put scissors, I put rock, I win!\n")
            bot_wins += 1
        
        else:
            print("\nThat wasnt a choice, make sure you are using 1,2, or 3.\n")

    if bot_wins >= 2:
        losses += 1
        print("You lose.\n\n")
        plays += 1

    elif plr_wins >= 2:
        print("You win!\n\n")
        wins += 1
        plays += 1



while True:

    play = input("Would you like to play a game of rock paper scissors (press Y for yes and N for no)\n").capitalize().strip()

    if play == "Y":

        if plays == 0:
            print(f"\n\nYou havent played me yet!\n\n")
            turn()

        elif plays > 0:
            print(f"\n\nYou have beat me {wins} times, and have lost to me {losses} times.\n\n")
            turn()

    elif play == "N":
        print("good night!")
        break

    else:
        print("That wasnt an option, make sure you are pressing Y or N.")