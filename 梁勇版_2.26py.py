import turtle
x,y = eval(input("Enter the coordinate of the center:"))
r = eval(input("Enter the radius of the circle:"))

turtle.showturtle()
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.write("({},{})".format(x,y))

turtle.penup()
turtle.goto(x,y - r)
turtle.pendown()
turtle.circle(r)

















turtle.done()
