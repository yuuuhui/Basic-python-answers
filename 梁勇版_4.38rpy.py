# Q39

import turtle

x1,y1,r1 = eval(input("Enter circle1's x-,y- coordinates, and radius: "))
x2,y2,r2 = eval(input("Enter circle2's x-,y- coordinates, and radius: "))

turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("r1:({},{})".format(x1,y1))

turtle.penup()
turtle.goto(x1,y1 - r1)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.write("r2:({},{})".format(x2,y2))

turtle.penup()
turtle.goto(x2,y2 - r2)
turtle.pendown()
turtle.circle(r2)

d12 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

turtle.penup()
turtle.goto(x1,(y1-r1))

turtle.pendown()


if 0 <= d12 <= r1:
    print("The center of circle2 inside the circle1 ")
    if x1 == x2 and y1 == y2 and r1 == r1:
        turtle.write("The circle1 overlaps completely with circle2.")
    elif (d12 + r2) > r1:
        turtle.write("The circle1 overlaps circle2")
    else:
        turtle.write("The circle2 inside circle1")
    
elif d12 > r1:
    print("The center of circle 1 outside the circle2")
    if d12 > (r1 + r2):
        turtle.write("The circle2 does not overlap the circle1")
    else:
        turtle.write("The circle1 overlaps circle2")
    
    
        
else:
    turtle.write("error occured")







turtle.done()
