def isprime(x):
    divisor = 2
    isp = True
    while divisor < x:
        if x % divisor == 0:
            isp =False
            break
        else:
            pass
        divisor += 1
    return isp
def meiprime(z):
    m = 2 **(z) - 1
    print("{:^9}".format(m),end = "\n")
print("p \t 2^(p) - 1")
y = 1
while y < 31:
    if isprime(y) == True:
        print(y,end = "\t")
        meiprime(y)
    y += 1






