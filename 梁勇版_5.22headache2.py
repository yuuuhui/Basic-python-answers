
from math import *




divisor = 2


for i in range(2,1000):

    if i % 2 == 0 and i != 2:
        continue
    elif i % 3 == 0 and i != 3:
        continue
    elif i % 5 == 0 and i != 5:
        continue
    elif sqrt(i) != int(sqrt(i)):
        
        print(i,end = " ")
    
