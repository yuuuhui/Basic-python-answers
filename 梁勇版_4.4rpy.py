import random

x = random.randint(0,100)
y = random.randint(0,100)
ans = eval(input("{} + {} =".format(x,y)))

sum = x + y

if ans == sum:
    print("correct answer!")
else:
    print("Wrong Answer")

