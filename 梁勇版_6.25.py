def isprime(n):
    isp = True
    
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            
            isp = False
            break
        else:
            isp = True
        divisor += 1
    return isp
    
    
            
            
    


"""def isprime(x):
    count = 0
    i = 0
    while count < 100:
        divisor = 2
        isprime = True
        i += 1
        while divisor < i:
            if i % divisor == 0:
                isprime = False
                break
            else:
                pass
            divisor += 1
        
       
        a = int(str(n)[::-1])
        
        
        if isprime == True:
            print(i,end = "\t")
            count += 1
            if count % 10 == 0:
                print("\n")
"""

def isreverse(x):
    a = int(str(x)[::-1])
    return a


count = 0
i = 1
while count < 100:
    i += 1
    isprime(i)
    x = isreverse(i)
    isprime(x)
    if isprime(i) == True and isprime(x) == True:
        print(i,end = "\t")
        count += 1
        if count % 10 == 0:
            print("\n")
    
    
    
