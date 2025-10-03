#MW_CP1 rock paper scissors


import random 
wins = 0
plr_wins = 0
bot_wins = 0
plays = 0

while True:
    play = input("Would you like to play a game of rock paper scissors (press Y for yes and N for no)").capitalize().strip()
    if play == "Y":
        if wins == 0 and plays == 0:
            print("you havent played me yet!")
            while plr_wins < 2 and bot_wins < 2:
                choice = input("press 1 for rock, press 2 for paper, and press 3 for scissors\n")
                if choice == "1" and random.randint(1,3) == 3:
                    print("you put rock, and I put scissors, you win!")
                    plr_win += 1
                elif choice == "1" and random.randint(1,3) == 2:
                    print("you put ")
    elif play == "N":
        pass
    else:
        pass