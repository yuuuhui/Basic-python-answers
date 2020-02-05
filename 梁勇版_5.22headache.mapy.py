
for i in range(2,1000):
    
    isprime = True
    divisor = 2
    while divisor < i:
        if i % divisor == 0:
            isprime = False
            break
        divisor += 1

    if isprime:
        print(i,end = " ")

    
