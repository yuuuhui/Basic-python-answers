from math import *
import turtle

turtle.penup()
turtle.goto(-175,0)
turtle.pendown()
turtle.goto(176,0)
turtle.dot()

turtle.penup()
turtle.goto(0,-60)
turtle.pendown()
turtle.goto(0,60)
turtle.dot()




turtle.penup()
turtle.goto(-175,50 * sin((-175 / 100) * 2 * pi))
turtle.pendown()

for x in range(-175,176):
    turtle.color("red")
    turtle.goto(x,50 * sin((x / 100) * 2 * pi))
    
turtle.color("black")
turtle.penup()
turtle.goto(-100,-15)
turtle.pendown()
turtle.write("-2\u03c0")

turtle.penup()
turtle.goto(100,15)
turtle.pendown()
turtle.write("-2\u03c0")

turtle.penup()
turtle.goto(-175,50 * cos((-175 / 100) * 2 * pi))
turtle.pendown()

for y in range(-175,176):
    turtle.color("blue")
    turtle.goto(y,50 * cos((y / 100) * 2 * pi))

    





turtle.done()
