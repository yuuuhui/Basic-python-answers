



for i in range(2,1000):
    d = 2
    isprime = True
    while d < i :
        if i % d == 0:
            isprime = False
            break
        
        else:
            pass
        d += 1
    if isprime == True:
        print(i,end = " ")
