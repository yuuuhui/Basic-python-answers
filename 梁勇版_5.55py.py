import turtle

turtle.showturtle()
step = 20
for i in range(8):
    for j in range(8):
        turtle.penup()
        turtle.speed (0)
        turtle.goto(i * step,j * step)
        turtle.pendown()
        turtle.begin_fill()
        if (i + j) % 2 == 0:
            turtle.color("white")
        else:
            turtle.color("black")
        for k in range(4):
            turtle.forward(step)
            turtle.right(90)
        turtle.end_fill()
"""turtle.color("black")
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
for s in  range(4):
    turtle.forward(step * 8)
    turtle.left(90)
"""

                    
turtle.done()



