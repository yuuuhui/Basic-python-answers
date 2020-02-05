import turtle
turtle.showturtle()
turtle.write("0,0")





for i in range(1,11):
    
    turtle.penup()
    turtle.goto(0,-20 * i)
    turtle.pendown()
    turtle.circle(20 * i)

turtle.done()
