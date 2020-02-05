
import turtle

turtle.showturtle()
turtle.write("0,0")
def turtlego(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def drawrect(x1 = 0,y1 = 0,width = 100,height = 100):
    turtlego(x1 + width / 2,y1 + height / 2)
    turtle.left(180)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)

def drawcircle(x2 = 50, y2 = 0,radius = 50):
    turtlego(x2,y2)
    turtle.write("50,0")
    turtlego(x2,y2 - radius)
    turtle.circle(radius)

drawrect() 
drawcircle()
turtle.done()
