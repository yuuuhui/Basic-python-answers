import turtle
r = int(input("Enter the radius:"))
turtle.showturtle()
turtle.circle(r)

turtle.penup()
turtle.goto(2 * r,0)
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(0,2 * r)
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(2 * r, 2 * r)
turtle.pendown()
turtle.circle(r)








turtle.done()
