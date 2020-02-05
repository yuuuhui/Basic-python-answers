n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))

if n1 < n2:
    d = n1
    while not( n1 % d == 0 and n2 % d == 0):
        d -= 1
            
        
    else:
        print("{} is the greatest common divisor".format(d))
            
        
     

elif n1 > n2:
    d = n2
    while not( n1 % d ==0 and n2 % d == 0):
        d -= 1
        
        
    else:
        print("{} is the greatest common divisor".format(d))

else:
    print("{} is the greatest common divisor".format(n1))
