


for i in range(10,101,10):#sub diff value
    e = 1
    for k in range(1,i + 1):# number of i 
        s = 1
        for h in range(1,k+1):
            s *= h
        print("s is",s) # s is the divisor
        e += 1 /s
        print("e is",e)
    
