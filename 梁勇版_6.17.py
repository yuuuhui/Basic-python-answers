side1,side2,side3 = eval(input("Enter three sides in double"))

def isarea(side1,side2,side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    print("The area of the triangle is",area)
    

def isvalid(side1,side2,side3):
    isValid = True
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        isValid = True
        

         
    else:
        isValid = False
    print(isValid)
    if isValid == True:
        isarea(side1,side2,side3)
isvalid(side1,side2,side3)
    
