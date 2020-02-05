x0,y0 = eval(input("Enter center of a circle  with two coordinates as x,y:"))

x1,y1 = eval(input("Enter a point with two coordinates as x,y:"))

d = ((x1 - x0) ** 2 + (y1 - y0) ** 2 ) ** 0.5


if d > 10:
    print("point({},{}) is not in the circle".format(x1,y1))
elif 0 < d < 10:
    print("point({},{}) is in the circle".format(x1,y1))
elif d ==10:
    print("point({},{}) is on the circle".format(x1,y1))

else:
    print("programming error!")
 
