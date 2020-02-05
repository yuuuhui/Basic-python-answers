x,y = eval(input("Enter a coordinates as x,y:"))



hd = abs(x)
vd = abs(y)

if 0 < x <= 5 and 0 < y <= 2.5:
    print("Point ({},{})is in the reactangle.".format(x,y))


    
else:
    print("Error occurs")
