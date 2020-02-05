import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(40,-69.28)
turtle.pendown()
turtle.write("(40,-69.28)")

turtle.penup()
turtle.goto(-40,-69.28)
turtle.pendown()
turtle.write("(-40,-69.28)")

turtle.penup()
turtle.goto(-80,-9.8)
turtle.pendown()
turtle.write("(-80,-9.8)")

turtle.penup()
turtle.goto(-40,69)
turtle.pendown()
turtle.write("(-40,69)")

turtle.penup()
turtle.goto(40,69)
turtle.pendown()
turtle.write("(40,69)")

turtle.penup()
turtle.goto(80,0)
turtle.pendown()
turtle.write("(80,0)")

turtle.color("red")
turtle.goto(40,69)
turtle.goto(-40,69)
turtle.goto(-80,-9.8)
turtle.goto(-40,-69.28)
turtle.goto(40,-69.28)
turtle.goto(80,0)


turtle.done()
