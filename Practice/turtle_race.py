# MW_CP1 Turtle race

#importing Turtle & random
import turtle
import random
#position variable
position = 0

#function for turtle win
def winner(racer):
    if racer.xcor() >= 300:
        return(f"{racer} has won")
    
#defining 5 turtles
finish_line = turtle.Turtle()

red = turtle.Turtle()
blue = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()
orange = turtle.Turtle()

#list of turtles 
turtles = [red, blue, green, purple, orange]

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

#function for moving turtles
def mover():
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(10,50))
            winner(turtle)
            if winner == f"{turtle} has won":
                victor = winner
                break
            else:
                continue
        if victor == True:
            break
        else:
            continue

mover()
