x1,y1 = eval(input("Enter x-,y- coordinates of center of a rectangle:"))


x2,y2 = eval(input("Enter x-,y- coordinates of a point"))



hd12 = abs(x1 - x2)
vd12 = abs(y1 - y2)



if 0 <= hd12 <= 50 and 0 <= vd <= 25:
    print("The point is within the rectangle.")
else:
    print("the point is not inside the reactangle.")





