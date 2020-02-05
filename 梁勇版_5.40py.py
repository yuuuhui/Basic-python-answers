from random import *

head = 0
tail = 0

for i in range(1,1000001):
    x = randint(0,1)
    if x == 0:
        head += 1
        
    else:
        tail += 1


print("The total number of head is {}".format(head))

print("The total number of tail is {}".format(tail))

"""sum = head + tail
print(sum)
"""
