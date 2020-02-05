def isprime(n):
    divisor = 2
    isp =True
    while divisor < n:
        if n % divisor == 0:
            isp = False
            break
        else:
            pass
        divisor += 1
    return isp
        
for i in range(1,100):
    k = i + 2
    if isprime(i) == True and isprime(k) == True:
        print("({},{})".format(i,k))
    
    
