

j = 1
count = 0
pi = 0 

for i in range(10000,100001,10000):
    for j in range(1, (2 * i),2):
        count += 1
        if count % 2 != 0:
            pi += 1/j
        else:
            pi += (- 1/j)
    pi *= 4
    print("when the value of i is {} ,value of pi is{}".format(i,pi))
    pi = 0
    
        
    
    
