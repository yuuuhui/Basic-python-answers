import turtle

def turtlegoto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    
def drawline(x1,y1,x2,y2,color = "black",size = 1):
    turtle.color(color)
    turtle.pensize(size)
    turtlegoto(x1,y1)
    turtle.goto(x2,y2)


def drawstar():
    drawline(0,100,50,-150)
    turtle.goto(-100,0)
    turtle.goto(100,0)
    turtle.goto(-50,-150)
    turtle.goto(0,100)

drawstar()

