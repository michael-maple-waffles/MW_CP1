#MW_CP1 Debugging practice


import random


def start_game():

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.\n\n")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    game_over = False

    while not game_over:
        
        guess = int(input("Enter your guess: "))#Guess was a string and therefore couldnt be used in future variables
        
        if attempts >= max_attempts:#if was attached to another if, making the condition not important, also needed an else.
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.\n")
            game_over = True
        
        else:#previous if didnt have this condition
           
            print(f"You have {max_attempts - attempts} attempts left.\n")
            
            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number! In {attempts} attempts.\n")
                game_over = True

            elif guess > number_to_guess:
                print(f"Too high! Try again.\n")
                
                attempts += 1#added because it made the previous conditional unusabel

            elif guess < number_to_guess:
                print(f"Too low! Try again.\n") 
                
                attempts += 1 #added because it made the previous conditional unusabel

            else: #previous conditional didnt have this condition
                print(f"That was an incorrect input, make sure you are using a number.\n")
        #"continue" was un important to the code

        

    print("Game Over. Thanks for playing!")

start_game()

#import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()