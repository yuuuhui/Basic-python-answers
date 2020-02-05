x1,y1,w1,h1 = eval(input("Enter r1's x-,y- coordinates,width,and height:"))
x2,y2,w2,h2 = eval(input("Enter r2's x-,y- coordinates,width,and height:"))






hd12 = abs(x2 - x1)
vd12 = abs(y2 - y1)


if 0 <= hd12 <= w1 /2 and 0 <= vd12 <= h1 / 2:
    print("The coordinate of center of the 2nd rect is within the 1st rect")
    if x1 == x2 and y1 == y2 and w1 == w2 and h1 == h2:
        print("r2 overlaps completely with r1")
    elif ((x2 + w2 / 2) > (x1 + w1 / 2)) or \
         ((x2 - w2 /2) < (x1 - w1 /2 )) or \
         ((y2 + h2 /2) > (y1 + h1 /2)) or \
         ((y2 - h2 /2) < (y1 - h1 /2)):
        print("r2 overlaps with r1")
    else:
        print("r2 is inside r1")
else:
    print("The coordinate of center of the 2nd rect is outside the 1st rect")
    if hd12 <= (w1/2 + w2 /2) or vd12 <=(h1/2 + h2 /2 ):
        print("r2 overlaps with r1")
    else:
        print("r2 is completely outside of  r1")
