x1,y1,w1,h1 = eval(input("Enter r1's x-,y- coordinates,width,and height:"))
x2,y2,w2,h2 = eval(input("Enter r2's x-,y- coordinates,width,and height:"))

hd12 = abs(x2 - x1)
vd12 = abs(y2 - y1)

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()



turtle.penup()
turtle.goto(x1 + w1 /2,y1)
turtle.pendown()
turtle.left(90)
turtle.forward(w1 /2)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(w1 /2)


turtle.penup()
turtle.goto(x2 + w2 /2,y2)
turtle.pendown()
turtle.left(90)
turtle.forward(w2 /2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(w2 /2)

turtle.penup()
turtle.goto((x1 + x2) / 1.4, (y1 + y2) / 1.4)
turtle.pendown()
turtle.pensize(10)
turtle.color("red")

if 0 <= hd12 <= w1 /2 and 0 <= vd12 <= h1 / 2:
    print("The coordinate of center of the 2nd rect is within the 1st rect")
    if x1 == x2 and y1 == y2 and w1 == w2 and h1 == h2:
       turtle.write("r2 overlaps completely with r1")
    elif ((x2 + w2 / 2) > (x1 + w1 / 2)) or \
         ((x2 - w2 /2) < (x1 - w1 /2 )) or \
         ((y2 + h2 /2) > (y1 + h1 /2)) or \
         ((y2 - h2 /2) < (y1 - h1 /2)):
        turtle.write("r2 overlaps with r1")
    else:
        turtle.write("r2 is inside r1")
else:
    print("The coordinate of center of the 2nd rect is outside the 1st rect")
    if hd12 <= (w1/2 + w2 /2) or vd12 <=(h1/2 + h2 /2 ):
        turtle.write("r2 overlaps with r1")
    else:
        turtle.write("r2 is completely outside of  r1")




turtle.done()
