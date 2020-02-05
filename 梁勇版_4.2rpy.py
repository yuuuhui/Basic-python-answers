import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)


sum = num1 + num2 + num3
ans = eval(input("Enter the answer of {}+{}+{}:".format(num1,num2,num3)))

if ans == sum:
    print("The answer is correct!")
else:
    print("Wrong answer!")
