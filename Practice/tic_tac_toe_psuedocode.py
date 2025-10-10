#MW_CP1 tic tac toe psuedo code


#Function to resart:
    #set all functions to = there base values, all lists shouldcontain no X's and O's everything should be how it was before.

#funtion to print and build board
    #show SPACE(1)|SPACE(2)|SPACE(3)
    #show -+-+-
    #show space(4)|SPACE(5)|SPACE(6)
    #show -+-+-
    #show space(7)|SPACE(8)|SPACE(9)

#function for a turn
    #ask user where they would like to place there X
    #if this is a number:
        #if PLAYER_INPUT is in SPACES:
            #replace space(number) with X
            #and remove PLAYER_INPUT from SPACES
        #else if this space is already taken:
            #force player to entry there input
    #else:
        #Force player to retry there input

#function for robot turn
    #ROBOT_CHOICE is a list of numbers 1-9 that will get removed as SPACES are taken out of its list.
    #replace SPACE with O where its location is equal to ROBOT_CHOICE


#function to check if player or bot has won.
    #WIN_CONDITIONS is equal to all the normal win conditions in tic tac toe, IE: 1,2,3 is win condition one and 4,5,6 is win condition two, so on so forth
    #loop for CONDITION in WIN_CONDITIONS
        #check if SPACE[CONDITION[1]] == SPACE[CONDION[2]] == SPACE[CONDITION[3]] == "X"
            #show "You Win!"
            #return True
        #check else if SPACE[CONDITION[1]] == SPACE[CONDION[2]] == SPACE[CONDITION[3]] == "0"
            #show "Oops, you lose..."
            #return True
    #if all(num in [X,O] for num in SPACE)
        #show oops a tie 
        #return True


#function to run the game
    #call function to restart
    #while win_conditions is False
        #Functin to show board.
        #function for turn
        #function for win check
        #function for robot turn
        #function for win check

#while true
    #ask if player wants to play
    #if player says yes call run game
    #else if player says no, break