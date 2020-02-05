import turtle

x1,y1 = eval(input("Enter the 1st point coordinate as x,y:"))
x2,y2 = eval(input("Enter the 2nd point coordinate as x,y:"))

turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("({},{}) ".format(x1,y1))

turtle.showturtle()
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.write("({},{}) ".format(x2,y2))

turtle.goto(x1,y1)



turtle.done()
