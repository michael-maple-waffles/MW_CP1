# MW_CP1 turtle notes

import turtle

turtle.shape("circle")
turtle.color("#F417CF")
turtle.pensize(10)
turtle.fillcolor("blue")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)

    turtle.right(90)
turtle.end_fill()

turtle.done()