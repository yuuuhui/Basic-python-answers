import turtle

turtle.showturtle()



x1,y1 = eval(input("Enter the coordinates of the  1st point as x,y:"))

x2,y2 = eval(input("Enter the coordinates of the 2nd point as x,y:"))

x3,y3 = eval(input("Enter the coordinates of the 3rd point as x,y:"))



turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("({},{})".format(x1,y1))

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.write("({},{})".format(x2,y2))



turtle.penup()
turtle.goto(x3,y3)
turtle.pendown()
turtle.write("({},{})".format(x3,y3))

turtle.goto(x2,y2)
turtle.goto(x1,y1)
turtle.goto(x3,y3)

side1 = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
side2 = ((y3 - y2) ** 2 + (x3 - x2) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

turtle.penup()
turtle.goto(x1 + 10,y1 + 10)
turtle.pendown()
turtle.write("the area of the triangle is {:.1f}".format(area))




turtle.done()
