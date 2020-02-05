import turtle

turtle.showturtle()

def turtlego(x1,y1):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()

def drawRectangle(color = "black",x = 0, y = 0, width = 30, height = 30):
    turtle.color(color)
    turtlego(x,y)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    
    



drawRectangle()

    
 
turtle.done()
