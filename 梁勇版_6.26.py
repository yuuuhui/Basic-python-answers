
def isprime(z):
    i = 2
    divisor = 2
    ispr = True
    while divisor < z:
        if z % divisor == 0:
            ispr =False
        else:
            pass
        divisor += 1
    return ispr
    

def ismeiprime(x):
    i = 2
    isp = True
    while 2 ** (i) - 1 <= x:
        if (2 ** (i) - 1 )== x and isprime(x) == True and i <= 31:
            isp = True
            
            print(i,end = "\t")
            print(2 ** (i) - 1,end = "\n")
            
            
            break
        else:
            isp = False
        i += 1
    return isp
count = 0

y = 3
print("p \t 2^p -1")
while count < 31:
    #ismeiprime(y)
    
    if ismeiprime(y) == True :
        
        
        count += 1
    else:
        pass
    y += 1
    
