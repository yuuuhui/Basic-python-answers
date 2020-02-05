import turtle

r = eval(input("Enter the radius of the rings:"))
turtle.showturtle()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.color("blue")
turtle.pensize(5)
turtle.circle(r)


turtle.penup()
turtle.goto(2 * r + 10,0)
turtle.pendown()

turtle.color("black")
turtle.pensize(5)
turtle.circle(r)

turtle.penup()
turtle.goto(4 * r + 20,0)
turtle.pendown()

turtle.color("red")
turtle.pensize(5)
turtle.circle(r)

turtle.penup()
turtle.goto(3 * r + 15,-r)
turtle.pendown()

turtle.color("green")
turtle.pensize(5)
turtle.circle(r)

turtle.penup()
turtle.goto(r + 5,-r)
turtle.pendown()

turtle.color("yellow")
turtle.pensize(5)
turtle.circle(r)




turtle.done()


