'''
地图网站 www.gps-data-team.com/map
68923,Atlanta NE in US,GPS Position: 99°24'18"W, 40°24'37"N for x1,y1
73073,Orlando OK in US,GPS Position: 97°24'29"W, 35°56'40"N for x2,y2
36033,Georgiana AL in US,GPS Position: 86°38'5"W, 31°37'28"N for x3,y3
78.11,Charlotte TX in US,GPS Position: 98°39'20"W, 28°48'51"N for x4,y4
'''

#atlanta 1 orlando 2 georgiana 3 charlotte 4

from math import *

x1,y1 = radians(99.405),radians(40.410)
x2,y2 = radians(97.408),radians(35.944)
x3,y3 = radians(86.634),radians(31.624)
x4,y4 = radians(98.656),radians(28.814)

r = 6371.01

d12 = r * ( acos(    sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos( y1 - y2 )    ))
d23 = r * ( acos(    sin(x2) * sin(x3) + cos(x2) * cos(x3) * cos( y2 - y3 )    ))
d34 = r * ( acos(    sin(x3) * sin(x4) + cos(x3) * cos(x4) * cos( y3 - y4 )    ))
d41 = r * ( acos(    sin(x4) * sin(x1) + cos(x4) * cos(x1) * cos( y4 - y1 )    ))
d24 = r * ( acos(    sin(x2) * sin(x4) + cos(x2) * cos(x4) * cos( y2 - y4 )    ))

s = (d12 + d24 + d41) / 2
area = ( s * (s - d12) * (s - d24) * (s - d41) ) ** 0.5

s2 = (d23 + d34 + d24 ) / 2
area1 = (s2 * (s2 - d23) * (s2 - d34) * (s2 - d24)) ** 0.5

tarea = area + area1
print("the area bounded by the four place is {}".format(tarea))




































'''
import turtle
turtle.screensize(10,10)

turtle.showturtle()
turtle.penup()
turtle.goto(99.405,40.410)
turtle.pendown()
turtle.write("99.405,40.410")

turtle.penup()
turtle.goto(97.408,35.944)
turtle.pendown()
turtle.write("97.408,35.944")

turtle.penup()
turtle.goto(86.634,31.624)
turtle.pendown()
turtle.write("86.634,31.624")

turtle.penup()
turtle.goto(98.656,28.814)
turtle.pendown()
turtle.write("98.656,28.814")

turtle.done()
'''


