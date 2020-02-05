from math import *
xsquare = 0
sum = 0

numlist = []
for i in range(1,11):
    num = eval(input("Enter ten numbers"))
    xsquare += (num ** 2)
    sum += num

mean = sum /10
sd = sqrt(   (   xsquare - ((sum ** 2)/10)   ) / (10 - 1))

print(mean,sd)
