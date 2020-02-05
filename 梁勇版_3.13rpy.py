import turtle


turtle.showturtle()

turtle.right(90)
turtle.penup()
turtle.goto(-30,30)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(100,steps = 6)

turtle.end_fill()


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.write("STOP",font = ("arial",40,"normal"))
turtle.end_fill()

turtle.hideturtle()









turtle.done()
