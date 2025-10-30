# MW_CP1 Turtle race

#importing Turtle & random
import turtle
import random
#position variable
position = 0

#function for turtle win

    
#defining 5 turtles
finish_line = turtle.Turtle()

red = turtle.Turtle()
blue = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()
orange = turtle.Turtle()

#list of turtles 
turtles = [red, blue, green, purple, orange]
turtles_indexed = ["red","blue", "green", "purple", "yellow"]

#turtle colors
red.color("red")
blue.color("blue")
green.color("green")
purple.color("purple")
orange.color("orange")

#turtle shapes & setting turtle position
for i in turtles:
    i.shape("turtle")

    i.penup()
    i.setposition(0,position)

    position += 20

    i.pendown()

#making the finish line
finish_line.penup()
finish_line.setposition(300,120)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(140)

def winner():
    indexed = 0
    for racer in turtles:
        indexed += 1

        if racer.xcor() >= 300:
            return indexed
        
        
#function for moving turtles
def mover():
    turn = 1
    victor = False
    while True:
        for turtle in turtles:
            if turn == 1:
                move = random.randint(10,18)
                turtle.forward(move)
                turn +=1
            else:
                move = random.randint(10,25)
                turtle.forward(move)
            if bool(winner()) == True:
                victor = bool(winner())
                break
            
            
        if victor == True:
            return f"{turtles_indexed[winner()-1]} has won"
        else:
            continue

print(mover())
