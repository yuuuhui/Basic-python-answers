integer = int(input("Enter an integer, the input ends if it is 0:"))
pnum = 0
nnum = 0
sum = 0
n = 0
while integer != 0:
    if integer > 0:
        pnum += 1
        sum += integer
        n += 1
        integer = int(input("Enter an integer, the input ends if it is 0:"))
        
    else:
        nnum += 1
        sum += integer
        n += 1
        integer = int(input("Enter an integer, the input ends if it is 0:"))
        
        

else:
    pass
average = sum / n 
print("the number of positive integer is {},\n the number of negative integer is {} \n the sum  is {} \n the average is {} ".format(pnum,nnum,sum,average))
