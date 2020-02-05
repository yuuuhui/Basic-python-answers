from random import *





def random(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))

for i in range(1,101):
    a = random('A','Z')
    print(a,end = " ")
    if i % 10 == 0:
        print("\n")
