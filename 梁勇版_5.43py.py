from random import *
from itertools import *


count = 0


for i in range(1,8):
    for k in range(1,8):
        if k == i:
            continue
        elif i == k and k == i:
            continue
        else:
            count += 1
            print(i,k)
print("The total nunmber of all combinations is {:.0f}".format(count / 2))
