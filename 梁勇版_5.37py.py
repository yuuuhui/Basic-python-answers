from math import *
sum = 0


for i in range(625,0,-1):
    
    sum += (1 / ( sqrt(i) + sqrt(i+1) ))
    print(sum)
            
