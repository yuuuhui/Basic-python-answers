

x0,y0,x1,y1,x2,y2 = eval(input("Enter the x,y coordinate of a line joining (x0,y0) and (x1,y1) \n and then determine  whether a point(x2,y2) is at which side of the line \
\n you may  enter the value as x0,y0,x1,y1,x2,y2:"))
de = (x1 -x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def leftoftheline(x0,y0,x1,y1,x2,y2):
    if de > 0:
        print("p2 is on the left side of the line")
    else:
        rightoftheline(x0,y0,x1,y1,x2,y2)
        
        
    
    


def rightoftheline(x0,y0,x1,y1,x2,y2):
    if de < 0:
        print("p2 is on the right side of the line")
    else:
        ontheline(x0,y0,x1,y1,x2,y2)
        
        


def ontheline(x0,y0,x1,y1,x2,y2):
    if  de == 0:
        print("p2 is on the right side of the line")
    else:
        leftoftheline(x0,y0,x1,y1,x2,y2)

leftoftheline(x0,y0,x1,y1,x2,y2)
