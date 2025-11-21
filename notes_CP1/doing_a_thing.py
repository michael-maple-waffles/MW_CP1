#MW_CP1


"""import turtle

turtle1 = turtle.Turtle()
turtle1.speed(1000)
turtle1.color("light blue")
turtle1.penup()
turtle1.goto(0,0)
turtle.pendown()

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle1.forward(length)
            draw_branch(length/3)
            turtle1.backward(length)
            turtle1.right(60)

for i in range(6):
    draw_branch(100)
    turtle1.right(60)

turtle1.hideturtle"""

#def function factorial(val)
def factorial(val):
    #for i in range(val)-1
    total = val
    for i in range(1,val):
        #total = total * i+1
        
        total = total * (i)
    #return total
    return total

#while True
while True:
    #user_val = input("what number would you like to input?")
    user_val = input("Input a number: ").strip()
    #if user_val is numeric:
    if user_val.isnumeric():
        #user_val = int(val)
        user_val = int(user_val)
        #factual = factorial(user_val)
        factual = factorial(user_val)
        #print(f"your original value is {user_val}, it as a factorial is: {factual}\n")
        print(f"\nYour starting number is {user_val}, it factorialized is: {factual}.\n")
    #else:
    else:
        #print("not valid, insure you are using a non negative integer number")
        print("not valid, ensure you are using a non negative integer number")
    

