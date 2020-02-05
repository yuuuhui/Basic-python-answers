
from math import *
x1,y1,x2,y2 = eval(input("Enter x1,y1,x2,y2 to determine the distance between two point:"))


def distance(x1,y1,x2,y2):
    distanc = (x1 - x2) ** 2 + (y1 - y2) ** 2
    distance = sqrt(distanc)
    print("The distance is",distance)

distance(x1,y1,x2,y2)
    
