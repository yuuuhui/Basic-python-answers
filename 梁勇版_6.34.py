from math import *
n = eval(input("Enter the number of sides:"))
s = eval(input("Enter the side:"))



def area(n,s):
    area = (n * (s ** 2)) / (4 * tan(pi / n))
    print("The area of the polygon is {:.2f}".format(area))


    
area(n,s)
