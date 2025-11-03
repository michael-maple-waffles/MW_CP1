#MW_CP1 Maze on turtle


#import libraries
import random
import turtle

#function that randomly generates every peice in a collumn or row
pick = (0,1)
row = [[1,1,1,1,1,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1]]
collumn = [[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]]

def generate(direction):
    global row
    global collumn
    counter = 0 
    checking = 0
    for direct in direction:
        if counter == 0:
            counter += 1
            continue
        elif counter < 8:
            for cord in direct:
                form = random.choice(pick)
                direction[counter[cord[checking]]] = form
                checking += 1
            counter += 1
        else:
            continue

#function to determine if everything is solvable
def isSolvable(grid_row, grid_collumn):
    size = len(grid_row) - 3
    visited = []
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size-1 and y == size-1:
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        if 

#function that makes the turtle build the maze