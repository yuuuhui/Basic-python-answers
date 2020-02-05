# h 是 边心距， a 是 边长， A 是 面积

import turtle
from math import *


r = eval(input("Enter the length from the center to a vertex:"))

s = 2 * r * sin( pi / 5)

area = 5 * s * s / (4 * tan( pi / 5))

print("The area of the pentagon is {:.2f}".format(area))

turtle.showturtle()
turtle.right(180)
turtle.circle(r,360,5)


#


turtle.left(144)
turtle.forward(s)
turtle.goto(0, - r )


turtle.write("r = {}".format(r))





