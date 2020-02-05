import turtle
from random import *

turtle.showturtle()
turtle.write("0,0")
turtle.penup()
turtle.goto(60,50)
turtle.pendown()
turtle.goto(-60,50)
turtle.goto(-60,-50)
turtle.goto(60,-50)
turtle.goto(60,50)




for i in  range(1,11):
    turtle.penup()
    x = randint(-60,60)
    y = randint(-50,50)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(2)











turtle.done()
