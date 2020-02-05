import random

num1 = random.randint(0,99)
num2 = random.randint(0,99)


sum = num1 * num2

ans = eval(input("{} * {} =".format(num1,num2)))

if ans == sum:
    print("correct answer")
else:
    print("wrong answer")
    
