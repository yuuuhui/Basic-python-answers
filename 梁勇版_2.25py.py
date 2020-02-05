l = eval(input("Enter the length of the rectangle:"))
w = eval(input("Enter the width of the rectangle:"))

x,y = eval(input("enter the coordinates of the start point:"))

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(x,y)
turtle.pendown()


turtle.forward(l)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l)
turtle.right(90)
turtle.forward(w)








turtle.done()
