import turtle
turtle.showturtle()

for i in range(0,190,10):
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
    turtle.goto(180,i )


for k in range(0,190,10):
    turtle.penup()
    turtle.goto(k,0)
    turtle.pendown()
    turtle.goto(k,180)
turtle.hideturtle()
    

turtle.done()
    
