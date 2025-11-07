#MW_CP1 Maze on turtle


#import libraries
import random
import turtle
import time

#function that randomly generates every peice in a collumn or row
pick = (0,1)
row = [[0,1,1,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,1,1,0]]
collumn = [[1,1,1,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,1,1,1]]

def generate(direction):
    global row
    global collumn
    counter = 0 
    checking = 0
    for direct in direction:
        checking = 0
        if counter == 0:
            counter += 1
            continue
        elif counter < 7:
            for cord in direct:
                form = random.choice(pick)
                direction[counter][checking] = form
                checking += 1
            counter += 1
        else:
            continue

#function to determine if everything is solvable
def isSolvable(grid_row, grid_collumn):
    size = len(grid_row) - 1
    visited = []
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size-1 and y == size-1:
            return True
        
        if (x,y) in visited:
            continue

        visited.append((x,y))

        if grid_collumn[x][y] == 0:
            stack.append((x-1,y))

        if grid_collumn[x+1][y] == 0:
            stack.append((x+1,y))

        if grid_row[y][x] == 0:
            if y != 0:
                stack.append((x,y-1))

        if grid_row[y+1][x] == 0:
            if y < 7:
                stack.append((x,y+1))
    else:
        return False


#function that makes the turtle build the maze
def maker(print_row, print_collumn):
    counting = 0
    counter = 0
    height = 0
    distance = 0
    for grid in print_row:
        for position in grid:
            if print_row[counting][counter] == 0:
                turtle.penup()
            else:
                turtle.pendown()
            
            turtle.forward(20)
            counter += 1

        counter = 0
        counting+=1
        height += 20
        turtle.penup()
        turtle.teleport(0,height)

    counting = 0
    counter = 0

    turtle.penup()
    turtle.teleport(0,0)
    turtle.left(90)
    for grid in print_collumn:
        for position in grid:
            if print_collumn[counting][counter] == 0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(20)
            counter+=1
        counting +=1 
        counter = 0
        distance += 20
        turtle.penup()
        turtle.teleport(distance,0)

#function that builds the game
def start():
    while True:
        generate(row)
        generate(collumn)
        select = isSolvable(row,collumn)
        if select == True:
            maker(row,collumn)
            time.sleep(2)
            break
        elif select == False:
            continue


#call start
start()

            

