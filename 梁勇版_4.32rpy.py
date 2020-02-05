x0,y0,x1,y1,x2,y2 =eval(input("Enter coordinates for the three points p0,p1 and p2:"))



de = (x1 -x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if de > 0:
    print("p2 is on the left side of the line")
elif de == 0:
    print("({},{}) is exactly on the line segment from({},{}) to ({},{})".format(x2,y2,x1,y1,x2,y2))
else:
    print("p2 is on the right side of the line")
