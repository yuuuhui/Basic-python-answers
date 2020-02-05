import turtle

turtle.showturtle()


turtle.right(180)
turtle.penup()
turtle.goto(10,10)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(50)
turtle.end_fill()


turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(50, steps = 5)
turtle.end_fill()

turtle.penup()
turtle.goto(-290,-20)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(50,steps = 3)
turtle.end_fill()



turtle.left(45)
turtle.penup()
turtle.goto(-240,-20)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(50,steps = 4)
turtle.end_fill()

turtle.left(105)
turtle.penup()
turtle.goto(100,-80)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(50,steps = 6)
turtle.end_fill()



'''
turtle.penup()
turtle.goto()
turtle.pendown()
turtle.circle(50)

'''



turtle.done()
