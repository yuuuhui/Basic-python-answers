from math import *
x1,y1 = eval(input("Enter point 1 (latitude and longitude:)"))
x2,y2= eval(input("Enter point 2 (latitude and longitude:)"))
x1 = radians(x1)
y1 = radians(y1)
x2 = radians(x2)
y2 = radians(y2)
                  

r = 6371.01
d = r * ( acos(    sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos( y1 - y2 )    ))
print("The distance between the two points is {} km".format(d))
