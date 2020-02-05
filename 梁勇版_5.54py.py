import turtle
from math import *


turtle.showturtle()

turtle.penup()
turtle.goto(-175,0)
turtle.pendown()
turtle.goto(175,0)
turtle.dot()

turtle.penup()
turtle.goto(0,-180)
turtle.pendown()
turtle.goto(0,180)
turtle.dot()

turtle.penup()
turtle.goto(-15,0.25 * 15 ** 2)
turtle.pendown()


for i in range(-15,20):
    turtle.goto(i, 0.25 * i ** 2)



turtle.done()
