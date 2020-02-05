import turtle

from random import * 
turtle.showturtle()
def turtlegoto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown
def getrandom(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))

for i in range(110,10,-10):
    for k in range(10,110,10):
        turtlegoto(k,i)
        a = getrandom('a','z')
        turtle.write("{:^2}".format(a))
    
    


turtle.done()
