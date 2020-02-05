


      
def sum(n):
    x = 0
    for i in range(1,10):
        if (n / (10 ** i)) > 1:
            x += 1 # x refers to 10 * x that the number can be =divided
    sums = 0
    for j in range(1,2 * (x+1)):
        if j % 2 != 0:
            y = n % 10
            sums += y
        else:
            n //= 10
    print(sums)
            
sum(2345)
        
        
         
        




