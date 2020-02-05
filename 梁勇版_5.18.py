#smallest factot list：2，3，5，7，11，13，17，18.......
num = int(input("Enter a number:"))
"""!= 1 and num != 0"""
print("the factor is ",end = "")
d = num
while num > 1:
    d -= 1
    if d <= 0 or d == 1:
        continue

    elif num % d == 0:

        if d >= 5 and (d % 2 == 0 or d % 3 == 0 or d % 5 == 0 ):
            continue
        else:
            print(d,end = " ")
            
    else:
        continue
        
     
        
            
    
else:
    if num == 1:
        print("1 itself and 1 is its only factor")
    else:
        print("not applicable")

        
    
        
