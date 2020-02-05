import turtle
step = 30
turtle.showturtle()
    
for i in range(8):
    for j in range(8):
        turtle.penup()
        turtle.goto(i * step,j * step)
        turtle.pendown()
        turtle.begin_fill()
        if (i + j) % 2 == 0:
            turtle.color("black")
        else:
            turtle.color("white")
        for k in range(4):
            turtle.forward(step)
            turtle.right(90)
        turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("black")
for i in range(4):
    turtle.forward(step * 8)
    turtle.left(90)

turtle.done()
