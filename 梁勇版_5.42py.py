from random import *




count = 0

for i in range(1,1000001):
    x = randint(1,8)
    if x > 0 and x <= 5:
        count += 1
    else:
        pass

print(count / i)
        
    
