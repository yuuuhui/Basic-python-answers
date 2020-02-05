from math import *
s = eval(input("Enter the side:"))
def area(s):
    area = ( 5 * (s ** 2) ) / (4 * tan(pi / 5) )
    print("The area of the pentagon is {:.2f}".format(area))

area(s)
    
    
    
